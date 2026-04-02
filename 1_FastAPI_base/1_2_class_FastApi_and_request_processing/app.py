import os.path

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "О сайте"}

def get_path_directory_without_filename():
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    script_path = get_path_directory_without_filename()
    print(script_path)

    uvicorn.run("1_2_class_FastApi_and_request_processing.main:app",
                host='127.0.0.1',
                port=80)
                #reload=True,
                #workers=1,)