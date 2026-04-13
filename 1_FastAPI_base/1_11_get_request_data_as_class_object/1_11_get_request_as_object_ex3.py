from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette.responses import FileResponse

# Пример 3 - валидация параметров и класс Field
class Person(BaseModel):
    name: str = Field(default="Undefined", min_length=3, max_length=20)
    age: int = Field(default=0, ge=18, lt=111)

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.post("/hello3")
def hello3(person: Person):
    return {"message": f"Привет, {person.name}, твой возраст - {person.age}"}

