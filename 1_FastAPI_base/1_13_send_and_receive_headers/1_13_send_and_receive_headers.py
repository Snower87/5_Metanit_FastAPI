from fastapi import FastAPI, Response, Header

app = FastAPI()

# Пример 1 - отправляется кастомный заголовок "Secret-Code"
@app.get("/1")
def read_root1():
    data = "Hello Metanit.com"
    return Response(content=data, media_type="text/plain", headers={"Secret-Code": "1234"})

# Пример 2 - задаем заголовки с помощью атрибута headers из класса Response
@app.get("/2")
def read_root2(response: Response):
    response.headers["Secret-Code"] = "1234"
    return {"message": "Hello MATANIT.com2"}

# Пример 3 - Получаем заголовок "User-Agent"
@app.get("/3")
def read_root3(user_agent: str = Header()):
    return {"User_agent": user_agent}
# Ответ в ввиде сообщения на странице: {"User_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"}

# Пример 4 - Получаем заголовок "Secret-Code"
@app.get("/4")
def root(secret_code: str | None = Header(default = None)):
    return {"Secret-Code": secret_code}
# Response: {"Secret-Code":null}
