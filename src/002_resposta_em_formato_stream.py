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

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Me fale mais sobre a criação dos computadores."},
    ],
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
