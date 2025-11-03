# https://platform.openai.com/docs/api-reference/chat
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
        {
            "role": "system",
            "content": "Você será um tradutor de textos de português para inglês. Apenas traduza e responda a tradução do texto que você receber."
        },
        {
            "role": "user",
            "content": "O livro está na mesa."
        },
    ],
    max_tokens=300,
    temperature=0.8
)

print(response.choices[0].message.content)
