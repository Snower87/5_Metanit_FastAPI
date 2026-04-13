from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse

# Пример 5: Получение вложенных списков

class Person(BaseModel):
    name: str
    languages: list = []
    # у атрибута можно установить значение по умолчанию на случай, если в запросе не содержится соответствующих данных:
    # - languages: list = ["Java", "Python", "JavaScript"]

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index5.html")

"""
Пример 5:
Отправка данных из javascript выглядела бы следующим образом:
const response = await fetch("/hello", {
    method: "POST",
    headers: { "Accept": "application/json", "Content-Type": "application/json" },
    body: JSON.stringify({ 
        name: "Tom",
        languages: ["Python", "JavaScript"]
    })
});
const data = await response.json();
console.log(data);      // {message: "Name: Tom. Languages: ['Python', 'JavaScript']"}
"""

@app.post("/hello5")
def hello5(person: Person):
    return {"message": f"Name, {person.name}. Languages: {person.languages}"}