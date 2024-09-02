# table formmation 
from sqlmodel import SQLModel,Field #type: ignore

class readStudents(SQLModel,table=True): #It is used to create table model for students in database
    id: int = Field(default=None,primary_key=True)
    name: str
    grade: str 
    rollNo: str
    marks: int
