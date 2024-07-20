from fastapi import FastAPI
import uvicorn
app=FastAPI()




# dynamic path is used to receive data from the frontend using path or url but it is not secured because of the security purpose
@app.get("/gettodos/{id}")
def getTodos(id):
    print("getTodos called",id)
    return id;



# query param is used to receive data from the frontend using query parameters but it is not secured because of the security purpose
@app.get("/")
def dataUsingQueryParam(studentName,rollNo):
    print("Data using query param",studentName,rollNo)
    return studentName+rollNo;









@app.post("/gettodos")
def getOneTodo():
    print("get one todo post called")
    return "get todo post called "


def start():
    uvicorn.run("uitclass.main:app",host="127.0.0.1",port=8080,reload=True) 