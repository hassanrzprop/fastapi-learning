# table formmation 
from sqlmodel import SQLModel,Field #type: ignore
class readStudents(SQLModel,table=True):
    id: int = Field(default=None,primary_key=True)
    name: str
    grade: str 
    rollNo: str
    marks: int
