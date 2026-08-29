import os
from google import genai
from dotenv import load_dotenv

# Cargar la API key desde el archivo .env
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

if not clave_api:
    raise ValueError("No se encontró GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=clave_api)
MODELO = "gemini-3.6-flash"

# Prompt Few-Shot: 3 ejemplos (positivo, neutral, negativo) para fijar el
# formato exacto de la respuesta (una sola palabra).
PROMPT_SENTIMIENTOS = """Eres un clasificador de sentimientos de reseñas de libros.
Responde ÚNICAMENTE con una de estas palabras: POSITIVO, NEUTRAL o NEGATIVO.
No agregues explicaciones ni frases adicionales.

Reseña: "Este libro cambió mi forma de ver la vida, una obra maestra total."
Sentimiento: POSITIVO

Reseña: "El libro estuvo bien, ni me encantó ni me decepcionó."
Sentimiento: NEUTRAL

Reseña: "Una pérdida de tiempo, la trama no tiene sentido y los personajes son planos."
Sentimiento: NEGATIVO

Reseña: "{resena}"
Sentimiento:"""

# El usuario puede escribir la reseña que quiera clasificar
resena_a_clasificar = input("Escribe la reseña del libro que quieres clasificar: ").strip()

if not resena_a_clasificar:
    resena_a_clasificar = "Este libro empezó bien pero el final fue muy apresurado y decepcionante."

try:
    response = client.models.generate_content(
        model=MODELO,
        contents=PROMPT_SENTIMIENTOS.format(resena=resena_a_clasificar)
    )
    print("✅ Respuesta del modelo:")
    print(response.text)
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")
