from fastapi import FastAPI,Body,Query,Path,HTTPException
from pydantic import BaseModel,Field
from typing import Annotated
import uvicorn

app=FastAPI()
# to use body parameter we need to define a class of items and then use it in function parameter  like in line 14 here we define a variable and then define the class we made over their here we use all three parameters 1)path 2)Querry 3)body PARAMETER


# data validation for body parameter
class Item(BaseModel):
    id:int
    title:str=Field(max_length=20,min_length=4)
    description:str=Field(max_length=100)
class User(BaseModel):
    name:str
    designation:str     
# body parameter doesn't went through the url so it is more secured for sensitive data
@app.get("/student/")
def todo(item: Item,user: User,count:Annotated[int,Body()]):
    print(user)
    print("hello world")
    return {"message":"Hello World!",
            "user":user,
            "Item_List":item,
            "count":count
            }
# here we applied string validation for item that it s max length 10 and min length 3 and pattern validation which means in which pattern should we enter a value in the string  start with "has" **alias is used to add result with another name for result 
@app.get("/queryAnnotated")
def queryTest(item_sf:Annotated[str,Query(alias="item-test" ,max_length=10,min_length=3,pattern="^has[a-z0-9A-Z]")]):
    # custom validation for item_sf
    if item_sf!="test":
        raise HTTPException(status_code=400,detail="invalid item NAME")
    return {"item":item_sf}


# PATH PARAMETER 
@app.get("/pathValidation/{valid}")
def pathValid(valid:Annotated[int,Path(ge=10,le=100)]):
    return valid
def start():
    uvicorn.run("todos.main:app",host="127.0.0.1",port=8080,reload=True)