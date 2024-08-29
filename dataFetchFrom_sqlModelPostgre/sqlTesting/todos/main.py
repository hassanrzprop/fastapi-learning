from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel,Field,create_engine,Session,select

connection_string='postgresql://postgres.vyocxeyiivvjrixbgpxt:JZvSYocLSxa4fE2R@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres' 
connection=create_engine(connection_string) #establishing connection with database

class homie(SQLModel,table=True):  # creating table
    id: int = Field(default=None,primary_key=True)
    name: str
    age: int
    is_Active: bool
SQLModel.metadata.create_all(connection)

app=FastAPI()
@app.get('/sql')
def to_sql():
    print("to_sql called")
    return{"message":"to sql called suceesfully"}
@app.get('/getStudents')
def getstudents():        #data read from data base
    with Session(connection) as session: #session is used to make short connection with database to get data only
        statement = select(homie).where(homie.id==2) #where is used to get specific data
        result=session.exec(statement)
        data=result.all()
        print(data)
        return data

def start():
    uvicorn.run("todos.main:app",host="127.0.0.1",port=8000,reload=True)
