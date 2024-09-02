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
    # this session is used to inertact with database and database and select is used to fetch data from tables in database
    with Session(engine) as session:
        num= id
        statement=select(readStudents)
        result=session.exec(statement) #exec is used to execute SQL statement and fetch data
        data= result.all() # all is used to fetch whole data
        return data
def start():
    create_tables() #here create_tables is placed because eveytime when sever starts it will automatically creates table
    uvicorn.run("todos.main:app",host="127.0.0.1",port=8080,reload=True) 