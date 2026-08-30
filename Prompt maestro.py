import os

from google import genai
from dotenv import load_dotenv

# Cargar API Key
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

if not clave_api:
    raise ValueError("No se encontró GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=clave_api)
MODELO = "gemini-3.6-flash"

# Entrada del usuario
situacion = input("Escribe la situación: ").strip()

# Prompt Maestro
PROMPT = f'''Eres un Gerente de Finanzas amable pero firme.

Tu tarea es redactar un correo profesional para un cliente a partir
de la situación proporcionada por el usuario.

### DATOS / SITUACIÓN DEL CLIENTE ###
{situacion}
###

El correo debe informar sobre el pago pendiente y solicitar su
regularización de manera cordial, clara y profesional.

Formato:
1. Asunto
2. Saludo
3. Cuerpo del correo
4. Despedida
5. Al final, incluye una tabla con el resumen de los montos adeudados.

Si la situación no contiene datos específicos como nombre, factura
o monto, no los inventes. Puedes utilizar expresiones generales
como "cliente" o "monto pendiente".

No agregues explicaciones sobre el prompt. Entrega directamente
el correo y la tabla.
'''

try:
    response = client.models.generate_content(
        model=MODELO,
        contents=PROMPT
    )

    print("\n========== RESULTADO ==========\n")
    print(response.text)

except Exception as e:
    print(f"❌ Ocurrió un error: {e}")