from sqlalchemy import Column, Integer, String, Boolean, Enum
from enum import Enum as PyEnum
from app.database import Base

class UserRole(PyEnum):
    user = "user"
    psychologist = "psychologist"
    admin = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    anonymous = Column(Boolean, default=True)
    name = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.user)
