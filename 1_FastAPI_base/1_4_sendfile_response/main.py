from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# 1. FileResponse в ответе
@app.get("/")
def root():
    return FileResponse("./index.html")

# 2. Альтернативный вариант с FileResponse
@app.get("/file", response_class=FileResponse)
def root_file():
    return FileResponse("./index.html")

# 3. Передача файла в виде потока байт
@app.get("/file/333")
def root_file_333():
    return FileResponse("./index.html",
                        filename="mainpage.html",
                        media_type="application/octet-stream",)

