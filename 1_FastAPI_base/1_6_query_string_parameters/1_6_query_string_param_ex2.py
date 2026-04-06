from fastapi import FastAPI, Query
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

# 4.1. Пример использования валидации Query
# min_length: устанавливает минимальное количество символов в значении параметра
# max_length: устанавливает максимальное количество символов в значении параметра
# pattern: устанавливает регулярное выражение, которому должно соответствовать значение параметра
# lt: значение параметра должно быть меньше определенного значения
# le: значение параметра должно быть меньше или равно определенному значению
# gt: значение параметра должно быть больше определенного значения
# ge: значение параметра должно быть больше или равно определенному значению
# Пример запроса: http://127.0.0.1:8000/users4?name=Tom
@app.get("/users4")
def get_users4(name: str = Query(min_length=3, max_length=10)):
    return {"user_name": name}

# 4.2. Перехват сообщения об ошибке
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "message": "Ошибка валидации входных данных",
            "details": exc.errors()
        },
    )

# 5. Валидация для 2х параметров (Query)
# Пример запроса - http://127.0.0.1:8000/users5?name=Tom&age=16
@app.get("/users5")
def get_users5(name: str = Query(min_length=3, max_length=10),
               age: int = Query(ge=3, le=20)):
    return {"user_name": name, "age": age}

# 6. Установить значение по умолчанию с помощью параметра default в Query:
# Если в запрошенном адресе отстуствует параметр name, то по умолчанию он будет равен строке "Undefined"
@app.get("/users6")
def get_users6(name: str = Query(default="Undefined", min_length=2, max_length=10)):
    return {"user_name": name}

# 7. Если параметр необязателен, то параметру default передается значение None:
@app.get("/users7")
def get_users7(name: str | None = Query(default=None, min_length=3)):
    if name is None:
        return {"user_name": "Undefined"}
    else:
        return {"user_name": name}