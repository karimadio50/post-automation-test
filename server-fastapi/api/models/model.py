import google.generativeai as genai
from diffusers import StableDiffusion3Pipeline,DiffusionPipeline,StableDiffusionPipeline
import torch
import os
from dotenv import load_dotenv
from datetime import datetime

#Load environment variables
load_dotenv()

#Fonction de génération d'image
def generate_image(text: str):
        model =DiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch", torch_dtype=torch.float16)
        #Utiliser le modèle avec un gpu
        #model.to(('cuda'))
        #Lancer la génération de l'image à partir du texte
        image = model(text).images[0]
        current_dir = os.getcwd()
        #static_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..', '..')), 'static')
        static_dir = os.path.join(current_dir,'static')
        #Sauvegarde de l'image
        name = datetime.now()
        image.save(os.path.join(static_dir, f"{name}.png"))
        return name

#Fonction de génération de texte
def generate_text(self, text: str) -> str:
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    #Configuration de la clé api de google
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)
    print(response.text)
    return response.text
   


#generate_image("femme")