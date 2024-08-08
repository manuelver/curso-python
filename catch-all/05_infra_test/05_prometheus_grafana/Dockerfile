# Usar imagen de python 3.9 slim
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente a /app
COPY app app

# Variables de entorno
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

# Comando para ejecutar la aplicación
CMD ["python", "app/main.py"]
