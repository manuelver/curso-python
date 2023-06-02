import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key

# modelos = openai.Model.list()

# print(modelos)

modelo = "text-davinci-002"
prompt = "Elige un buen nombre para un elefante"

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=3,  # Opcional. Número de respuestas
    temperature=1,  # Opcional. Controla la creatividad de la respuesta
    max_tokens=50  # Opcional. Número máximo de tokens en la respuesta
)

# print(respuesta)

# texto_generado = respuesta['choices'][0]['text']
# print(texto_generado)


for idx, opcion in enumerate(respuesta.choices):
    texto_generado = opcion.text.strip()
    print(f"Respuesta {idx + 1}: {texto_generado}\n")
