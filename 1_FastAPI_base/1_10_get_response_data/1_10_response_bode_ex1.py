from fastapi import FastAPI, Body
from starlette.responses import FileResponse

app = FastAPI()

# Пример 1.1 - При обращении по пути "/" клиенту будет отправляться страница index.html для ввода данных.
@app.get("/")
def root():
    return FileResponse("public/index.html")

# Пример 1.2 - Для обработки полученных в POST-запросе данных по адресу "/hello" определена функция hello()
@app.post("/hello")
def hello1(data = Body()):
    name = data["name"]  # для получения значения свойства "name", обращаемся по ключу: "name"
    age = data["age"]
    return {"message": f"{name}, ваш возраст - {age}"}

# Пример 2 - получение отдельных значений (embed=True)
# В примере 2 мы получали все данные из тела запроса в один параметр. Однако, установив параметр embed=True, можно получать отдельные значения:
@app.post("/hello2")
def hello2(name = Body(embed=True), age = Body(embed=True)):
    return {"message": f"{name}, ваш возраст - {age}"}

# Пример 3 - Валидация
@app.post("/hello3")
def hello3(name: str = Body(embed=True, min_length=3, max_length=20),
           age: int = Body(embed=True, ge=18, lt=111)):
    return {"message": f"{name}, ваш возраст - {age}"}