from fastapi import FastAPI
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем модель, объекты которой будут храниться в БД
class Base(DeclarativeBase): pass
class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

# Создаем таблицы
#Base.metadata.create_all(bind=engine)

# Создаем подключение (сессию) к БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

##################################
# *   CRUD. Добавление данных  * #
##################################

# Пример 1. Создаем объект Person и добавляем его в БД
tom = Person(name="Tom", age=20)
db.add(tom)     # сохраняем объект в БД
db.commit()     # сохраняем изменения
db.refresh(tom) # обновляем состояние объекта "tom"
                # и потом можем получить его новое состояние
print(tom.id)   # получаем установленный id

# Пример 2. Добавляем 2 объекта: "bob", "sam"
bob = Person(name="Bob", age=42)
sam = Person(name="Sam", age=25)
db.add(bob)     # сохраняем объект в БД
db.add(sam)
db.commit()     # сохраняем изменения
db.refresh(bob)
print(f"name: {bob.name}, age: {bob.age}")

# Пример 3. Добавление нескольких объектов в БД: add_all()
alice = Person(name="Alice", age=33)
kate = Person(name="Kate", age=28)
db.add_all([alice, kate])
db.commit()
db.refresh(alice)
print(f"name: {alice.name}, age: {alice.age}")

##################################
# *   CRUD. Получение данных   * #
##################################

# Пример 4. all(). Получение все данных:
people = db.query(Person).all()
for person in people:
    print(f"{person.id}. {person.name} ({person.age})")

# Пример 5. get(). Получения объекта по id
# получение одного объекта по id
first_person = db.get(Person, 1)
print(f"id = 1. {first_person.name} - {first_person.age}")

# Пример 6. filter(). Фильтрация среди всех значений по Person.age > 30
people6 = db.query(Person).filter(Person.age > 30).all()
print("Example 6: people with age > 30")
for p in people6:
    print(f"{p.id}. {p.name} ({p.age})")

# Пример 7. first(). Получение первого объекта с id = 1
first = db.query(Person).filter(Person.id==1).first()
print(f"{first.name} ({first.age})")

# методы get() и first() возвращают None, если объект не найден.
# Поэтому при получении одиночного объекта желательно проверять его на значение None.

###################################
# *   CRUD. Обновление данных   * #
###################################

# Пример 8. commit(). Обновление данных
# 1. Получаем первый объект с именем "Tom"
tom8 = db.query(Person).filter(Person.id==1).first()
print(f"{tom8.id}. {tom8.name} ({tom8.age})")  # 1.Tom (38)

# 2. Изменяем Тома )
tom8.name = "Tomas"
tom8.age = 22

# 3. Сохраняем изменения
db.commit()

# 4. Проверяем изменения. Получаем объект по "Tomas"
tomas = db.query(Person).filter(Person.name == "Tomas").first()
print(f"{tom8.id}. {tom8.name} ({tom8.age})") # "Tomas" (22)

##################################
# *   CRUD. Удаление данных    * #
##################################

# Пример 9. delete(). Обновление данных
bob9 = db.query(Person).filter(Person.name == "Bob").first()
# 1. Удаляем объект
db.delete(bob9)
# 2. Сохраняем изменения в БД
db.commit()
print(f"delete object with Person.name = 'Bob'")

# приложение, которое ничего не делает :)
app = FastAPI()

