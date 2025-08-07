from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from sqlalchemy.exc import IntegrityError, DataError
from fastapi import HTTPException, status

def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        anonymous=user.anonymous,
        name=user.name,
        hashed_password=get_password_hash(user.password),
        role=user.role.value if hasattr(user.role, 'value') else user.role 
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        if "UNIQUE constraint failed: users.email" in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database integrity error"
        )
    except DataError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid data format"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
