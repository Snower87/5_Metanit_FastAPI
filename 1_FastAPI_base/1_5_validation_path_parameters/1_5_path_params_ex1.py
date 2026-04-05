from fastapi import FastAPI

app = FastAPI()


# 1. Передаче параметра в путь url
@app.get("/users/{id}")
def get_user1(id: int):
    return {"user_id": id}

# 2. Пример передачи нескольких параметров: name, age
@app.get("/users/{name}/{age}")
def get_users2(name, age):
    return {"user_name": name, "user_age": age}

# 3. Пример передачи нескольких параметров через разделитель "--"
@app.get("/users/{name}--{age}")
def get_users3(name, age):
    return {"user_name": name, "user_age": age}