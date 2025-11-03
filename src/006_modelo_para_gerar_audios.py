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

response = client.audio.speech.create(
    # https://platform.openai.com/docs/models/tts-1
    model="tts-1",
    voice="ash",
    input="Estou acompanhando essa integração do Python com o OpenAI.",
)

response.write_to_file("meu_audio.mp3")
