from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class RoleEnum(str, Enum):
    user = "user"
    psychologist = "psychologist"
    admin = "admin"

class UserBase(BaseModel):
    anonymous: bool = True
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: RoleEnum 
class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
