from typing import Union

from fastapi import APIRouter, FastAPI

# router = APIRouter
app = FastAPI


class PostGenerator:

    def __init__(self, name: str):
        self.name = name
        self.router = APIRouter()
        self.router.add_api_route("/hello", self.hello, methods=["GET"])

    def hello(self):
        return {"Hello": self.name}

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
