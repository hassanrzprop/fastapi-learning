from fastapi import FastAPI,Path
import uvicorn
from typing import Optional,Annotated
from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
    id: int
    title: str
    description: str

stu: dict[str, str | int] = {
    "name": "Hassan_Raza",
    "age": 23
}

@app.get("/gettodos")
def getTodos(firstName: Optional[str] = None):
    print("gettodos called")
    return firstName

# python types
car: dict[str, int | str] = {         # produces error while defining data types in dictionary
    "model": "Tesla model S",
    "manufactureDate": 2023
}

def getUserFullname(firstName: str, lastName: str):
    return firstName + " " + lastName

students: list[str] = ["Hassan", "raza", "farukh"]

def start():
    uvicorn.run("uitclass.main:app", host="127.0.0.1", port=8080, reload=True)

# pytdantic models
# producing errors while defining data types in dictionary 
# from pydantic import BaseModel

# class Todo(BaseModel):
#     id: int
#     title: str
#     description: str

# external_data={
#     "id":1,
#     "title":"Learn FastAPI",
#     "description":"file to Learn FastAPI types"
# }
# user=Todo(**external_data)

userName:Annotated[str,"this is company employee name"]="ali"
num:Annotated[int,Path(ge=10)]=55
print(num)