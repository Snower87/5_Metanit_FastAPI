from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse


# Пример 1,2 - объявление класа с обязательным пар-ом (name), и необязательным атрибутом (age)
class Person(BaseModel):
    name: str
    age: int | None = None

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")

"""
Пример 1:
// отправляем запрос
const response = await fetch("/hello3", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            name: username,
            age: userage
        })
    });
    if (response.ok) {
        const data = await response.json();
        document.getElementById("message").textContent = data.message;
    }
    else
        console.log(response);
"""

# Пример 1 - Оба пар-ра (name, age) - обязательные
@app.post("/hello1")
def hello1(person: Person):
    return {"message": f"Привет, {person.name}, твой возраст - {person.age}"}

# Пример 2 -
@app.post("/hello2")
def hello2(person: Person):
    if person.age is None:
        return {"message": f"Привет, {person.name}"}
    else:
        return {"message": f"Привет, {person.name}, твой возраст - {person.age}"}