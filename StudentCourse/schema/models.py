from pydantic import BaseModel

class Student(BaseModel):
    name:str
    roll:int
    course:str