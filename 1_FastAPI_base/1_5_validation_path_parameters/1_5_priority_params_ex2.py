from fastapi import FastAPI

app = FastAPI()

# 1. Чтобы обрабатывалась /users/admin раньше, ее надо перенести вверх

# 2. Обработка "/users/admin" идет первой в очереди и поэтому обрабатывается
@app.get("/users/admin")
def root_admin():
    return {"message": "Hello to Admin"}

# 3. Обработка всех /users/{name}, кроме "/users/admin"
@app.get("/users/{name}")
def users(name):
    return {"user_name": name}