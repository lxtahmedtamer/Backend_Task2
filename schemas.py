from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    age: int
    greeting: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
