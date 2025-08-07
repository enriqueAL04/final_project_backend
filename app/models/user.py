from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    anonymous = Column(Boolean, default=True)  
    name = Column(String, nullable=True)       
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String)
