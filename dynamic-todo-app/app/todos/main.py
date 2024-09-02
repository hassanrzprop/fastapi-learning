from fastapi import FastAPI #type: ignore
import uvicorn #type: ignore
from sqlmodel import Session,select #type: ignore
from dotenv import load_dotenv #type: ignore
load_dotenv()
from .config.db import create_tables,engine
from .models.students import readStudents
    
app=FastAPI()
@app.get("/getstudent")
def getTodos():
    with Session(engine) as session:
        num= id
        statement=select(readStudents)
        result=session.exec(statement)
        data= result.all()
        return data
def start():
    create_tables()
    uvicorn.run("todos.main:app",host="127.0.0.1",port=8080,reload=True) 