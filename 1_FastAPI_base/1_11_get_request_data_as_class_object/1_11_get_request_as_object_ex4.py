from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette.responses import FileResponse

# Пример 4 - Получение списков объектов
class Person(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index4.html")

@app.post("/hello4")
def hello4(people: list[Person]):
    print(people)
    return {"message": people}

"""
Response в DevTools:
{
    "message": [
        {
            "name": "Tom",
            "age": 38
        },
        {
            "name": "Bob",
            "age": 41
        },
        {
            "name": "Sam",
            "age": 25
        }
    ]
}
"""