from typing import Union
from api.services.post_generator_service import PostGeneratorService
from api.controllers.post_controller import PostGenerator
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()
generator = PostGeneratorService()


# def runner():
#     app = FastAPI()
#     hello = PostGenerator("World")
#     app.include_router(hello.router)



@app.get("/generate-post")
def read_root(texte):
   generator.generate_post_text(texte)
   return 

@app.get("/get_files/{id}")
def view_image(id):
    name = [file.split(".")[0] for file in os.listdir(os.path.join(os.getcwd(),'static'))]
    image_path = os.path.join(os.getcwd(),'static', f'{id}.png')
    if image_path.split("/")[-1].split(".")[0] in name:
        return FileResponse(image_path)
    print(image_path.split("/")[-1])


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


