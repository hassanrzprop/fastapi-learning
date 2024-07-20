from fastapi import FastAPI
import uvicorn
app=FastAPI()
student=[{"rollNo":'234',"userName":"Ali"}]
@app.get("/")
def showStudents():
    print("student list called",student)
    return student
@app.get("/addStudent/")
def getTodos(rollNo: str,userName: str):
    dicion={"rollNo":rollNo,"userName":userName}
    student.append(dicion)
    print("getTodos called",rollNo,userName)
    return rollNo+userName;
def start():
    uvicorn.run("studentapp.main:app",host="127.0.0.1",port=8080,reload=True) 