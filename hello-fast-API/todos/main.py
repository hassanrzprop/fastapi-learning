from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get("/gettodos")
def getTodos():
    print("getTodos called")
    return "gettodos called"
@app.post("/gettodos")
def getOneTodo():
    print("get one todo post called")
    return "get todo post called "


def start():
    uvicorn.run("todos.main:app",host="127.0.0.1",port=8080,reload=True) 