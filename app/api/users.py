from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.database import SessionLocal
from app.crud.user import create_user, get_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    allowed_roles = {"user", "psychologist", "admin"}
    if user.role not in allowed_roles:
        raise HTTPException(status_code=400, detail="Invalid role")
    
    db_user = create_user(db, user)
    return db_user

@router.get("/{id}", response_model=UserOut)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
