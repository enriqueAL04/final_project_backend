from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    anonymous: bool = True
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: str 

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
