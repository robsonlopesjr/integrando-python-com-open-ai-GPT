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
            "content": "Dê respostas técnicas sobre programação. Se comporte como um programador Python experiente, especialista em padrões de projetos e arquitetura limpa."
        },
        {"role": "user", "content": "Me mostre como posso fazer um projeto Django com as melhores boas práticas."},
    ],
)

print(response.choices[0].message.content)
