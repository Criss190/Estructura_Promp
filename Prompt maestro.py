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

# Función para pedir los datos del cliente al usuario

def pedir_datos_cliente():
    """Recoge la información necesaria para redactar el correo."""
    nombre = input("Nombre del cliente: ").strip()
    empresa = input("Empresa del cliente: ").strip()
    factura = input("Número de factura: ").strip()
    monto = input("Monto adeudado: ").strip()
    fecha = input("Fecha de vencimiento: ").strip()
    motivo = input("Motivo breve del correo: ").strip()

    return nombre, empresa, factura, monto, fecha, motivo


nombre, empresa, factura, monto, fecha, motivo = pedir_datos_cliente()

# Prompt Maestro: usa los pilares Persona, Tarea, Contexto y Formato.
# El delimitador ### separa los datos del cliente del resto de la instrucción.
prompt_parte1 = f"""
Persona: Eres un Gerente de Finanzas amable pero firme.

Tarea: Escribe un correo dirigido a un cliente que tiene una factura pendiente
de pago, solicitando el pago de forma clara y profesional.

Contexto: El cliente mantiene una relación comercial activa con la empresa y
se busca conservar una buena relación mientras se resuelve el pago pendiente.

###
Datos del cliente:
Nombre: {nombre}
Empresa: {empresa}
Factura pendiente: {factura} por {monto}
Fecha de vencimiento: {fecha}
Motivo del correo: {motivo}
###

Formato: El correo debe finalizar con un resumen en formato de tabla que
muestre el número de factura, el monto adeudado y la fecha de vencimiento.
"""

try:
    response = client.models.generate_content(
        model=MODELO,
        contents=prompt_parte1
    )
    print("✅ Respuesta del modelo:")
    print(response.text)
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")