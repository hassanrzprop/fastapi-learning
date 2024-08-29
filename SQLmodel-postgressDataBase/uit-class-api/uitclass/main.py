from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/model")
def model():
    return "Model running properly"

def start():
    uvicorn.run("uitclass.main:app", host="127.0.0.1",port=8000 ,reload=True)