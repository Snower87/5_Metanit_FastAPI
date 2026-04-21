# 1. Импортируем зависимости
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String

from fastapi import FastAPI

# 2. Прописываем путь подключения к sqlite
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Для sqlite строка подключения начинается с sqlite://, затем идет относительный или абсолютный путь к файлу:
# sqlite:///относительный_путь/file.db
# sqlite:////абсолютный_путь/file.db

# строка подключения к postgresql
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 3.1 Создаем движок для sqlite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
    # предназначен только для SQLite. Указывает, что для взаимодействия с базой данных SQLite
    # в рамках одного запроса может использоваться больше одного потока.
)

# 3.2 Создаем движок для работы с другими СУБД
#engine2 = create_engine(SQLALCHEMY_DATABASE_URL)

# 4. Создаем базовый класс для моделей. Определение моделей
class Base(DeclarativeBase): pass

# 5. Cоздаем модель, объекты которой будут храниться в бд
class Person(Base):
    __tablename__ = "people"   # Атрибут __tablename__ хранит имя таблицы,

    # primary_key=True  указывает, что данный столбец будет представлять первичный ключ
    # параметр index=True говорит, что для данного столбца будет создаваться индекс.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

# 6. создаем таблицы
Base.metadata.create_all(bind=engine)
# Параметр - bind принимает класс, который используется для подключения к базе данных

# 7. Запускаем fastapi-приложение
app = FastAPI()