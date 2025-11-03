import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path


# Carrega o .env
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)
API_KEY = os.environ.get('API_KEY')

client = OpenAI(
    api_key=API_KEY
)

response = client.images.generate(
    # https://platform.openai.com/docs/models/dall-e-3
    model="dall-e-3",
    prompt="um programador com seu laptop, no estilo futurista",
    size="1024x1024",
    quality="standard",
    n=1,  # quantidade de imagens
)

print(response.data[0].url)
