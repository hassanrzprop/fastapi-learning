from fastapi import FastAPI,Query
from typing import Optional
import uvicorn
app=FastAPI()



# type validation on quer and path parameters
@app.get("/{student_id}")
def gettodos(student_id: int,rollNo: int,testResult: bool,optional: str | None=None,name: Optional[str]=None):
    print("get todos")
    return {
        "result":"working properly",
        "student_id":student_id,
        "name":name,
        "rollNo":rollNo,
        "test":testResult,
        "optional":f"{optional} if no value provided,it will be none"
    }
def start():
    uvicorn.run("uitclass.main:app", host="127.0.0.1",port=8000,reload=True)