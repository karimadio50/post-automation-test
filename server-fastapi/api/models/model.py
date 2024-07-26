import google.generativeai as genai
from diffusers import StableDiffusion3Pipeline,DiffusionPipeline,StableDiffusionPipeline
import torch
import os
from dotenv import load_dotenv
from datetime import datetime

#Load environment variables
load_dotenv()
model_texte = genai.GenerativeModel('gemini-pro')
model_image =DiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch", torch_dtype=torch.float16)


#Fonction de génération d'image
def generate_image(text: str):
        #Utiliser le modèle avec un gpu
        #model.to(('cuda'))
        #Lancer la génération de l'image à partir du texte
        image = model_image(text).images[0]
        current_dir = os.getcwd()
        #static_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..', '..')), 'static')
        static_dir = os.path.join(current_dir,'static')
        #Sauvegarde de l'image
        name = datetime.now()
        image.save(os.path.join(static_dir, f"{name}.png"))
        return name

#Fonction de génération de texte
def generate_text(text: str) -> str:
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    #Configuration de la clé api de google
    genai.configure(api_key=GOOGLE_API_KEY)
    response = model_texte.generate_content(text)
    print(response.text)
    return response.text
   


#generate_image("femme")
#result = generate_text("je veux que tu me génère une lettre de motivation \n je veux postuler pour un poste de développeur backend python/django dans une entreprise.\n Je suis développeur IA junior avec deux ans d'expériences minimum avec pour langage python et j'ai déjà travaillé sur des projets backend avec django")
# GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)
# chat = model_texte.start_chat(history=[])
# prompt = "je veux faire un post sur LinkedIn pour un projet de vision par ordinateur sur lequel j'ai travaillé"
# response = chat.send_message(prompt)
# response.text
# image = generate_text(f"je veux que tu me génère un prompt pour générer une image qui cadre avec ce post '{result}'")
# image
#result