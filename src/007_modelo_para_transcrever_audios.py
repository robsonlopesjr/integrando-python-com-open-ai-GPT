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

audio_file = open("meu_audio.mp3", "rb")

transcription = client.audio.transcriptions.create(
    # https://platform.openai.com/docs/models/whisper-1
    model="whisper-1",
    file=audio_file
)

print(transcription.text)
