# Utiliza una imagen base de Python en Alpine
FROM python:3.12.4-alpine

WORKDIR /app

# Instala bash, herramientas de compilación y librerías necesarias
RUN apk update && \
    apk upgrade && \
    python -m venv /env && \
    /env/bin/pip install --upgrade pip

# Añade el archivo de requisitos a la imagen
COPY requirements.txt /app/requirements.txt

RUN /env/bin/pip install --no-cache-dir -r /app/requirements.txt

# Añade el resto del código de la aplicación
COPY . /app

# Configura el entorno virtual
ENV VIRTUAL_ENV=/env
ENV PATH=/env/bin:$PATH

# Comando por defecto para ejecutar el bot
CMD ["python", "main.py"]
