from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel,Field,create_engine,select,Session

# creating connection with database
connection_string='postgresql://postgres.jplyqugllkunxxpgjqij:hassanraza3830@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres'
connection=create_engine(connection_string)

# table formmation 
class readStudents(SQLModel,table=True):
    id: int = Field(default=None,primary_key=True)
    name: str
    grade: str 
    rollNo: str
    marks: int
SQLModel.metadata.create_all(connection)
app=FastAPI()
app.get("/")
def hello():
    print("hello!")
    return "Hello World!"
@app.get("/getstudent/{id}")
def getTodos(id: int):
    with Session(connection) as session:
        statement=select(readStudents).where(readStudents.id==id)
        result=session.exec(statement)
        return result
@app.post("todos/")
def getOneTodo():
    print("get one todo post called")
    return  "oe"
def start():
    uvicorn.run("todos.main:app",host="127.0.0.1",port=8080,reload=True) 