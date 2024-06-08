import uvicorn
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello Jason"

@app.get("/test")
def test(name: str , family: str):
    return f'{family} {name}'


# if __name__ == "__main__":
#     uvicorn.run("main:app", port=5000, log_level="info")