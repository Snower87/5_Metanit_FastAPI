from fastapi import FastAPI
from starlette import status
from starlette.responses import RedirectResponse, PlainTextResponse

app = FastAPI()

# Пример 1. Переадресация с "/old" на -> "/new"
# Для переадресации в приложении FastAPI применяется класс RedirectResponse (класс-наследник от Response). В качестве
# обязательного параметра конструктор RedirectResponse принимает адрес для перенаправления
@app.get("/old")
def old():
    return RedirectResponse(url='/new') # или просто "/new"

@app.get("/new")
def new():
    return PlainTextResponse('Новая страница')

# Пример 2. Переадресация по абсолютному адресу
@app.get("/old2")
def old2():
    return RedirectResponse("https://metanit.com/python/fastapi")

# Пример 3.1 Изменяем статус-код в ответе при переадресации
@app.get("/old31")
def old31():
    return RedirectResponse("/new", status_code=302) # status_code=status.HTTP_302_FOUND

# Пример 3.2 Или так
@app.get("/old32", response_class= RedirectResponse, status_code=302)
def old32():
    return "/new"

