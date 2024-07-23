import os
from ..models.model import generate_image, generate_text

class PostGeneratorService:

    #Chargement du modèle de génération d'image
    #model_image = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    #Chargement du modèle de génération de texte

    def __init__(self):   
        pass

    def generate_post_image(self,  text: str):
        image = generate_image(text) #image contient l'identifiant de l'image généré
        return image

    def generate_post_text(self, text: str) -> str:
        texte = generate_text(text)
        return texte

# app = PostGeneratorService()

# liste = os.listdir(os.path.join(os.getcwd(),'server-fastapi','static'))
# for file in liste:
#     print(file.split(".")[0])