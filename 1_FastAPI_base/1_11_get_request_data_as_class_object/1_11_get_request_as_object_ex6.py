from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse

# Пример 6 - Вложенные модели
class Company(BaseModel):
    name: str

class Person(BaseModel):
    name: str
    company: Company

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index6.html")

"""
Пример 6:
const response = await fetch("/hello6", {
    method: "POST",
    headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({ 
        name: "Tom",
        company: {name: "Google"}
    })
});
const data = await response.json();
console.log(data);
"""

@app.post("/hello6")
def hello6(person: Person):
    return {"message": f"Name, {person.name}. ({person.company.name})"}