## 1) Requisitos

Necesitas Python 3 y acceso a una API Key de Gemini.

## 2) Crear el entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install google-genai python-dotenv
```

### Ubuntu / Debian

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install google-genai python-dotenv
```

### Fedora

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install google-genai python-dotenv
```

## 3) Configurar la API Key

Crea un archivo llamado `.env` en la raíz del proyecto y agrega lo siguiente:

```env
GEMINI_API_KEY=tu_clave_real_aqui
```

Importante:
- no pongas espacios alrededor del `=`
- no subas el archivo `.env` a GitHub
- el proyecto ya incluye `.gitignore` para proteger `.env` y `venv/`

## 4) Ejecutar cada script

### Windows

```bash
python "Prompt maestro.py"
python "Condicional .py"
python "Sentimientos.py"
python "Ensayos.py"
```

### Ubuntu / Fedora

```bash
python "Prompt maestro.py"
python "Condicional .py"
python "Sentimientos.py"
python "Ensayos.py"
```

Si prefieres usar Python 3 explícito:

```bash
python3 "Prompt maestro.py"
python3 "Condicional .py"
python3 "Sentimientos.py"
python3 "Ensayos.py"
```

## 6) Recomendación en VS Code

Selecciona como intérprete del proyecto:

```text
venv/bin/python
```

Esto asegura que todas las librerías se instalen dentro del entorno virtual y no a nivel global del sistema.

## 7) Nota final

Si vas a ejecutar el proyecto en Linux, usa el entorno virtual activo antes de correr los scripts:

```bash
source venv/bin/activate
```

Luego ejecuta cualquiera de los archivos anteriores.