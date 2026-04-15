from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

# 1. Необходимо установить модуль python-multipart с помощью команды:
#    pip install python-multipart

app = FastAPI()

@app.get("/")
def read_root1():
    return FileResponse("public/index.html")

# Пример 1 - Прием данных с формы Form()
# Причем параметры называются также, как и атрибуты name у полей формы. А самим параметрам присваивается объект Form.
@app.post("/postdata1")
def postdata(username = Form(), userage=Form()):
    return {"name": username, "age": userage}

"""
Валидация по параметрам
min_length: устанавливает минимальное количество символов в значении параметра
max_length: устанавливает максимальное количество символов в значении параметра
pattern: устанавливает регулярное выражение, которому должно соответствовать значение параметра
lt: значение параметра должно быть меньше определенного значения
le: значение параметра должно быть меньше или равно определенному значению
gt: значение параметра должно быть больше определенного значения
ge: значение параметра должно быть больше или равно определенному значению
"""
# Пример 2 - валидация параметров
# Пример 3 - значения по умолчанию
@app.post("/postdata2")
def postdata2(username: str = Form(default="Undefined", min_length=2, max_length=20),
              userage: int = Form(ge=18, lt=111)):
    return {"name": username, "age": userage}
