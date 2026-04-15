from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

# Пример 4 - отправка списка
@app.get("/")
def read_root4():
    print("start code: ex4")
    return FileResponse("public/index4.html")

@app.post("/postdata4")
def postdata4(username: str = Form(),
             languages: list = Form()):
    return {"name": username, "languages": languages}