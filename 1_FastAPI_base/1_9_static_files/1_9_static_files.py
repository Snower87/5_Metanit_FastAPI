from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Пример 1 - при обращении по пути "/static" приложение будет посылать в ответ файлы из каталога "public".
app.mount("/static1", StaticFiles(directory="/example"))

# Пример 2 - Получение файла index.html (при выставленном параметре html=True)
# Если значение html=True, то сервер автоматически отправляет файл index.html (при его наличии)
# Если значение html=False (по умолчанию), то сервер не отправляет index.html
# Теперь мы можем обратиться по пути http://127.0.0.1:8000/static/, и сервер также пришлет нам страницу index.html:
app.mount("/static2", StaticFiles(directory="example", html=True))

# Пример 3 - установить главную страницу для всего веб-приложения
app.mount("/", StaticFiles(directory=".", html=True))
