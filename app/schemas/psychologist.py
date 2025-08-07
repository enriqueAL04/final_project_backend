from pydantic import BaseModel, EmailStr

class PsychologistBase(BaseModel):
    name: str
    email: EmailStr
    is_volunteer: bool = True

class PsychologistCreate(PsychologistBase):
    password: str

class PsychologistOut(PsychologistBase):
    id: int

    class Config:
        orm_mode = True
