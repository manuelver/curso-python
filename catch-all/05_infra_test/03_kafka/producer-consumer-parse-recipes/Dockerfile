# Usa una imagen base de Python
FROM python:3.9-slim

# Configura el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script de Python al contenedor
COPY producer-consumer-parse-recipes.py /app/

# Comando por defecto para ejecutar el script
CMD ["python", "producer-consumer-parse-recipes.py"]
