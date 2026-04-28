import os
import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse

# 1. Структура данных (Person)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())


# 2. Условная база данных - набор объектов Person
people = [Person("Tom", 38),
          Person("Bob", 42),
          Person("Sam", 28)]


# 3. Метод для поиска пользователя в списке people
def find_person(id):
    for person in people:
        if person.id == id:
            return person
    return None

app = FastAPI()

# Получаем путь к директории, где лежит текущий файл
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "public", "index.html")

# 4. GET "/" - первый метод, который возвращает страницу
# "index.html"
@app.get("/")
async def main():
    return FileResponse(INDEX_PATH)

# 5. GET "/api/users" - получение всех пользователей
@app.get("/api/users")
def get_people():
    return people

# 6. GET "/api/users/{id}" - получение ползователя по {id}
@app.get("/api/users/{id}")
def get_person(id):
    # получаем пользователя по id
    person = find_person(id)
    print(person)
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}
        )
    # если пользователь найден, отправляем его
    return person

# 7. POST "/api/users" - добавление пользователя в нашу базу
@app.post("/api/users")
def create_person(data=Body()):
    person = Person(data["name"], data["age"])
    # добавляем объект в список people
    people.append(person)
    return person

# 8. PUT "/api/users" - изменение данных о пользователе
@app.put("/api/users")
def edit_person(data=Body()):
    # получаем пользователя по id
    person = find_person(data["id"])
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}
        )
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    return person


# 9. DELETE "/api/users/{id}" - Удаление пользователя
@app.delete("/api/users/{id}")
def delete_person(id):
    # получаем пользователя по id
    person = find_person(id)

    # если не найден, отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}
        )

    # если пользователь найден, удаляем его
    people.remove(person)
    return person