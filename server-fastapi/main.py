from typing import Union

from api.controllers.post_controller import PostGenerator
from fastapi import FastAPI

app = FastAPI()


# def runner():
#     app = FastAPI()
#     hello = PostGenerator("World")
#     app.include_router(hello.router)


@app.post("/generate-post")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}