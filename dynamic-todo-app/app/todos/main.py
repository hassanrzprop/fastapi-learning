from fastapi import FastAPI,HTTPException #type: ignore
import uvicorn #type: ignore
from sqlmodel import Session,select #type: ignore
from dotenv import load_dotenv #type: ignore
load_dotenv()
from .config.db import create_tables,engine
from .models.students import readStudents,updateStudents    
    
app=FastAPI()
@app.get("/getStudent")
def getTodos():
    # this session is used to inertact with database and database and select is used to fetch data from tables in database
    with Session(engine) as session:
        num= id
        statement=select(readStudents)
        result=session.exec(statement) #exec is used to execute SQL statement and fetch data
        data= result.all() # all is used to fetch whole data
        return data;
@app.post("/createStudent/") #data create function through frontend
def create_student(todoCreate:readStudents):
    with Session(engine) as session:
        session.add(todoCreate)
        session.commit()
        session.refresh(todoCreate)
        return{"message": "Student created successfully","id":todoCreate.id}
@app.put("/updateStudent/{id}")
def update_student(id: int,todoUpdate:updateStudents):
    with Session(engine) as session:
        db_todo=session.get(readStudents,id)
        if not db_todo:
            raise HTTPException(status_code=404,details="student not found")
        todo_data=todoUpdate.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return{"status":200,"message":"student updated successfully"};
@app.delete("/deleteStudent/{id}")
def delete_student(id: int):
    with Session(engine) as session:
        db_todo=session.get(readStudents,id)
        if not db_todo:
            raise HTTPException(status_code= 404, details="student not found")
        session.delete(db_todo)
        session.commit()
        session.refresh(db_todo)
        return{"status":200,"message":"student deleted successfully"};



def start():
    create_tables() #here create_tables is placed because eveytime when sever starts it will automatically creates table
    uvicorn.run("todos.main:app",host="127.0.0.1",port=8080,reload=True) 