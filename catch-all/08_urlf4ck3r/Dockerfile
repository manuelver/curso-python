# Usa una imagen base de Python oficial
FROM python:3.9-slim
ARG maintaner="manuelver"

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt /app

# Instala las dependencias del script
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script al contenedor
COPY urlf4ck3r.py /app

# Da permisos de ejecución al script
RUN chmod +x urlf4ck3r.py

# Define el comando predeterminado para ejecutar el script con argumentos
ENTRYPOINT ["./urlf4ck3r.py"]

# Especifica el comando por defecto, que puede ser sobreescrito al correr el contenedor
CMD ["-h"]
