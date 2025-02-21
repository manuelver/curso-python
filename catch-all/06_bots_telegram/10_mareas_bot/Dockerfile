# Usamos una imagen de Python oficial basada en Alpine
FROM python:3.9-alpine

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos y lo instalamos
COPY requirements.txt .

# Instalamos las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos de la aplicación
COPY ./bot /app  

# Comando para ejecutar el programa
CMD ["python", "bot.py"]
