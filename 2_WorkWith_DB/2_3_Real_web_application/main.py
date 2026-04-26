from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import FileResponse, JSONResponse

from database import *

# 1. Создаем все необходимые таблицы в БД (если они отстуствуют)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 2. Далее через get_db() объект сессии БД будет передаваться в функцию обработки:
# 1. Данный объект будет внедрен в функцию обработки запроса.
# 2. Выражение yield будет выполняться при получении КАЖДОГО нового запроса.
def get_db():
    db = SessionLocal()
    try:
        # помещение выражение yield в блок try позволяет получить и обработать любую ошибку,
        # возникшую в процессе взаимодействия с базой данных.
        yield db  # --> с помощью yield возвращаем созданный объект
    finally:
        # После завершения операций с базой данных выполняется блок finally,
        # в котором закрывается подключение к базе данных с помощью метода close()
        db.close()

# 3. Отправляется в ответ файл index.html, с помощью которого происходит основное взаимодействие с сервером (БД)
@app.get("/")
def main():
    return FileResponse("public/index.html")

# 4. GET "/api/users" - получение всех пользователей (список объектов Person, который отправляется клиенту)
@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    return db.query(Person).all()

# 5. GET "/api/users/{id}" - получение пользователя по id
@app.get("/api/users/{id}")
def get_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
    # если пользователь не найден, то отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Person not found"})
    # если пользователь найден
    return person

# 6. POST "/api/users" - добавление данные из этого запросе для создания объекта Person для создания пользователя
@app.post("/api/users")
def create_person(data = Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], age=data["age"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person

# 7. PUT "/api/users" - обновляем данные о пользователе из запроса
@app.put("/api/users")
def edit_person(data = Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == data["id"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Person not found"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    db.commit() # сохраняем изменения
    db.refresh(person)
    return person

# 8. DELETE "/api/users/{id}" - удаляем его {id} из базы данных и посылаем клиенту.
@app.delete("/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Пользователь не найден"})
    # если пользователь найден, удаляем его
    db.delete(person)   # удаляем объект
    db.commit()         # сохраняем изменения
    return person