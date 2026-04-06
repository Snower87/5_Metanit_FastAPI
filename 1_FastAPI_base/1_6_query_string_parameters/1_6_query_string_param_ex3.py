from fastapi import FastAPI
from fastapi.params import Path, Query

app = FastAPI()

# 8. Получение списков значений
# Путь запроса: http://127.0.0.1:8000/users8?people=first&people=2&people=33
@app.get("/users8")
def get_users8(people: list[str] = Query()):
    return {"people": people}

# 9. Сочетание Path + Query
# Путь запроса: http://127.0.0.1:8000/users9/Tom?age=38
@app.get("/users9/{name}")
def get_users9(name: str = Path(min_length=3, max_length=20),
               age: int = Query(ge=18, lt=111)):
    return {"name": name, "age": age}
