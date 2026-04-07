from fastapi import FastAPI
from fastapi.openapi.models import Response
from fastapi.params import Path
from starlette import status
from starlette.responses import JSONResponse

# Отправка статусных кодов:
# 1xx: предназначены для информации. Ответ с таким кодом не может иметь содержимого
# 2xx: указывает на успешноее выполнение операции
# 3xx: предназначены для переадресации
# 4xx: предназначены для отправки информации об ошибок клиента
# 5xx: предназначены для информации об ошибках сервера

# По умолчанию функции обработки отправляют статусный код 200, но при необходимости мы можем отправить любой статусный код.
# Для этого у методов get(), post(), put(), delete(), options(), head(), patch(), trace() в классе FastAPI применяется
# параметр status_code, который принимает числовой код статуса HTTP

app = FastAPI()

# Пример 1. Статус ответа 404 и сообщение
@app.get("/notfound", status_code=404)
def not_found1():
    return {"message": "Page not Found"}

# В FastAPI есть модуль status, в котором определены константы:
# HTTP_100_CONTINUE (код 100)
# HTTP_101_SWITCHING_PROTOCOLS (код 101)
# HTTP_102_PROCESSING (код 102)
# HTTP_103_EARLY_HINTS (код 103)
# HTTP_200_OK (код 200)
# HTTP_201_CREATED (код 201)
# HTTP_202_ACCEPTED (код 202)
# HTTP_300_MULTIPLE_CHOICES (код 300)
# HTTP_301_MOVED_PERMANENTLY (код 301)
# HTTP_302_FOUND (код 302)
# HTTP_400_BAD_REQUEST (код 400)
# HTTP_401_UNAUTHORIZED (код 401)
# HTTP_402_PAYMENT_REQUIRED (код 402)
# HTTP_403_FORBIDDEN (код 403)
# HTTP_404_NOT_FOUND (код 404)
# HTTP_405_METHOD_NOT_ALLOWED (код 405)
# HTTP_500_INTERNAL_SERVER_ERROR (код 500)
# HTTP_501_NOT_IMPLEMENTED (код 501)
# HTTP_502_BAD_GATEWAY (код 502)
# HTTP_503_SERVICE_UNAVAILABLE (код 503)
# HTTP_504_GATEWAY_TIMEOUT (код 504)
# HTTP_505_HTTP_VERSION_NOT_SUPPORTED (код 505)

# Пример 2. Использование статус-кода (константы) в декораторе
# В примере функция вне зависимости от данных запроса или каких-то других условий в любом случае возвращала статусный код 404.
# Однако это не всего бывает удобно
@app.get("/notfound2", status_code=status.HTTP_404_NOT_FOUND)
def not_found2():
    return {"message": "Использование константы: status.HTTP_404_NOT_FOUND"}

# Пример 3. Определение статусного кода в ответе
@app.get("/notfound3")
def not_found3():
    return JSONResponse("Статус-код в ответе", status_code=status.HTTP_404_NOT_FOUND) # или status_code=404

# Пример 4. Комбинация обоих подходов
# Если параметр пути меньше 1, то условно считаем, что переданные некорректные данные, и отправляем в ответ статусный код 400 (Bad Request)
@app.get("/users/{id}", status_code=200)
def get_usersId4(id: int = Path(gt=0)) -> JSONResponse:
    if id < 10:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Incorrect Data"})
    return JSONResponse(content={"message": f"Id = {id}"})