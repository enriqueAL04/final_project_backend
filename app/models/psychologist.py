from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Psychologist(Base):
    __tablename__ = "psychologists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    is_volunteer = Column(Boolean, default=True) 
    hashed_password = Column(String)
