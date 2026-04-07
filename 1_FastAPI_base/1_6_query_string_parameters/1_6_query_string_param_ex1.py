from fastapi import FastAPI

app = FastAPI()

# 1. Получение/Передача 2х параметров в запросе
# Строка запроса: http://127.0.0.1:8000/users?name=Tom&age=32
@app.get("/users")
def get_users(name, age):
    return {"user_name": name, "age": age}

# 2. Значения по-умолчанию
# В предыдущем примере 1, если мы не передадим хотя бы один из параметров, то мы получим ошибку
# Чтобы ошибки не было, можно задать для параметров значения по умолчанию
# !! Параметры со значению по умолчанию должны идти после обязательных параметров.
@app.get("/users2")
def get_users2(name = "undefuned", age = 18):
    return {"user_name": name, "age": age}

# 3. Ограничения по типу
@app.get("/users3")
def get_users3(name: str, age: int = 18):
    return {"user_name": name, "age": age}
