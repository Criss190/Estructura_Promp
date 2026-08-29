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

# Función para pedir el texto del usuario

def pedir_texto():
    """Pide un correo o mensaje para clasificarlo."""
    return input("Escribe el mensaje o correo de soporte: ").strip()


texto_usuario = pedir_texto()

# Prompt con lógica condicional SI/ENTONCES. El texto de entrada va delimitado por """.
prompt_parte2 = f'''Contexto: Eres un asistente de triaje de correos electrónicos de soporte.

Instrucciones: Se te proporcionará un texto delimitado por comillas triples (""").

1. SI el texto contiene una queja sobre un pago o factura:
   - Clasifícalo como "URGENTE-FINANZAS".
   - Extrae el número de factura si existe.
2. SI NO, si el texto es una duda técnica general:
   - Clasifícalo como "SOPORTE-ESTÁNDAR".
   - Responde exactamente: "Gracias, un técnico lo revisará".
3. SI NO es ninguna de las anteriores:
   - Responde simplemente: "Categoría no identificada".

No agregues explicaciones adicionales a la clasificación.

Texto del usuario:
"""
{texto_usuario}
"""
'''

try:
    response = client.models.generate_content(
        model=MODELO,
        contents=prompt_parte2
    )
    print("✅ Respuesta del modelo:")
    print(response.text)
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")