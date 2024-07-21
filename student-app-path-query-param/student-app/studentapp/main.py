from fastapi import FastAPI
import uvicorn
app=FastAPI()

students = [
    {"rollNo": '234', "userName": "Ali"},
    {"rollNo": '324', "userName": "waqar"},
    {"rollNo": '3878', "userName": "haider"},
    {"rollNo": '312', "userName": "huzaifa"}
]


@app.get("/")
def showStudents():
    print("student list called",students)
    return students
@app.get("/addStudent/")
def getTodos(rollNo: str,userName: str):
    dicion={"rollNo":rollNo,"userName":userName}
    students.append(dicion)
    print("getTodos called",rollNo,userName)
    return rollNo+userName;

@app.get("/updateStudent/{oldRollNo}/{newRollNo}/{newUserName}")
def update_student(oldRollNo: str, newRollNo: str, newUserName: str):
    for student in students:
        if student["rollNo"] == oldRollNo:
            student["rollNo"] = newRollNo
            student["userName"] = newUserName
            return {"message": f"Student {oldRollNo} updated successfully to {newRollNo} and {newUserName}"}
    return {"error": "Student not found"}
def start():
    uvicorn.run("studentapp.main:app",host="127.0.0.1",port=8080,reload=True) 



