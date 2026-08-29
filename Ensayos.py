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

# Prompt con rol, entrada delimitada, condicional de palabras y salida JSON.
PROMPT_EVALUADOR = '''Eres un Evaluador académico de ensayos.

Se te proporcionará un ensayo delimitado por comillas triples (""").

SI el ensayo tiene menos de 100 palabras:
- Recházalo.
- Pide que se envíe más contenido.

SI el ensayo tiene 100 palabras o más:
- Evalúalo bajo estos tres criterios: Ortografía, Coherencia y Argumentación.

Responde ÚNICAMENTE con un objeto JSON con las claves "nota_final" y
"comentarios". No agregues texto antes ni después del JSON.

Ensayo:
"""
{ensayo}
"""
'''


def pedir_ensayo():
    """Pide el ensayo por consola."""
    ensayo = input("Escribe tu ensayo: ").strip()
    if not ensayo:
        return "Este ensayo trata sobre la importancia de la educación en la vida de las personas. Explica cómo el conocimiento abre oportunidades y fortalece la autonomía, la responsabilidad y la participación ciudadana."
    return ensayo


ensayo_usuario = pedir_ensayo()

try:
    response = client.models.generate_content(
        model=MODELO,
        contents=PROMPT_EVALUADOR.format(ensayo=ensayo_usuario)
    )
    print("✅ Respuesta del modelo:")
    print(response.text)
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")