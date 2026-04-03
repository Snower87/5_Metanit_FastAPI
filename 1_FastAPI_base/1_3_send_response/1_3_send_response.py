import json_encoder
from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse, PlainTextResponse, HTMLResponse

app = FastAPI()

# 1. Стандартный вариант
@app.get("/")
def root():
    return {"message": "Hello World"}

# 2. Через кодировщик fastapi.encoders.jsonable_encoder
@app.get("/123")
def root123():
    data = {"message": "Hello World"}
    json_data = jsonable_encoder(data)
    return JSONResponse(status_code=200, content=json_data)

# 3. Передать данные в JSONResponse напрямую - без явной сериализации
@app.get("/222")
def root222():
    return JSONResponse(content={"message": "Hello World"})

# 4. Ответ в формате "Response"
"""
- content: задает отправляемое содержимое
- status_code: задает статусный код ответа
- media_type: задает MIME-тип ответа
- headers: задает заголовки ответа
"""
@app.get("/444")
def root444():
    data = "Hello, metanit"
    return Response(content=data, media_type="text/plain")

# 5. Ответ в формате "PlainTextResponse"
@app.get("/555")
def root555():
    data = "Hello 555"
    return PlainTextResponse(content=data, media_type="text/plain")

# 6. Ответ в формате "HTMLResponse"
# Он устанавливает для заголовока Content-Type значение text/html
@app.get("/666")
def root666():
    data = "<h3> Hello 666 </h3>"
    return HTMLResponse(content=data)

# 7. Задание класса ответа в декораторе метода
# Методы FastAPI такие как get(), post() и т.д. позволяют задать тип ответа с помощью параметра response_class:
@app.get("/777.1", response_class=PlainTextResponse)
def root7771():
    return "Hello 777.1"

@app.get("/777.2", response_class=HTMLResponse)
def root7772():
    return "<h3> Hello 777.2 </h3>"