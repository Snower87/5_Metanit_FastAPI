from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return HTMLResponse("<h2> Hello METANIT.com</h2>")

def get_current_fullpath():
  """
  Возвращает полный путь к текущему запускаемому Python-скрипту (папка + py.файл)
  """
  return os.path.abspath(__file__)

def get_path_directory_without_filename():
  """
  Возвращает путь к каталогу, в котором находится текущий запускаемый Python-скрипт.
  """
  return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
  script_path = get_path_directory_without_filename()
  print(f"{script_path}")