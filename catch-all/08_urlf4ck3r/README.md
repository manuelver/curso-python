# 🕸️ URLf4ck3r 🕵️‍♂️

> Repositorio original: [URLf4ck3r](https://github.com/n0m3l4c000nt35/urlf4ck3r)

URLf4ck3r es una herramienta de reconocimiento diseñada para escanear y extraer URLs del código fuente de sitios web.

📝 **Tabla de contenidos**
- [🕸️ URLf4ck3r 🕵️‍♂️](#️-urlf4ck3r-️️)
  - [🚀 Características principales](#-características-principales)
  - [📋 Requisitos](#-requisitos)
  - [🛠️ Instalación](#️-instalación)
  - [💻 Uso](#-uso)
  - [Con docker](#con-docker)
    - [Construir la imagen de Docker](#construir-la-imagen-de-docker)
    - [Ejecutar el contenedor](#ejecutar-el-contenedor)
    - [Ejecutar con Docker Compose:](#ejecutar-con-docker-compose)


## 🚀 Características principales

- 🔍 Escaneo recursivo de URLs
- 🌐 Detección de subdominios
- ✍️ Detección de palabras sensibles en los comentarios
- 🔗 Clasificación de URLs absolutas y relativas
- 💠 Detección de archivos JavaScript
- 🎨 Salida colorida para una fácil lectura
- ⏱️ Interrumpible en cualquier momento


## 📋 Requisitos

- Python 3.x
- Bibliotecas: `requests`, `beautifulsoup4`, `pwntools` (Ver en el fichero [requirements.txt](requirements.txt))


## 🛠️ Instalación

1. Descarga esta carpeta
2. Instalá las dependencias:

```
pip install -r requirements.txt
```

3. Haz el script ejecutable:

```
chmod +x urlf4ck3r.py
```

4. Para ejecutar el script desde cualquier ubicación:

- Mueve el script a un directorio que esté en el PATH, por ejemplo:
  ```
  sudo mv urlf4ck3r.py /usr/bin/urlf4ck3r
  ```
- O añade el directorio del script al PATH editando el archivo `.bashrc` o `.zshrc`:
  ```
  echo 'export PATH=$PATH:/ruta/al/directorio/de/urlf4ck3r' >> ~/.bashrc
  source ~/.bashrc
  ```


## 💻 Uso

Si seguiste el paso 4 de la instalación, puedes ejecutar el script desde cualquier ubicación simplemente con:

```
urlf4ck3r -u <URL> -o output.txt
```

De lo contrario, desde el directorio donde se encuentra ubicado el script:

```
./urlf4ck3r.py -u <URL> -o output
```

Ejemplo:

```
urlf4ck3r -u https://ejemplo.com -o output.txt
```

## Con docker

### Construir la imagen de Docker

Para construir la imagen desde el Dockerfile, navega al directorio donde se encuentra tu Dockerfile y ejecuta el siguiente comando:

```sh
docker build -t urlf4ck3r .
```

### Ejecutar el contenedor

Después de construir la imagen, puedes ejecutar tu script dentro de un contenedor de la siguiente manera:

```sh
docker run --rm urlf4ck3r -u https://ejemplo.com -o output.txt
```

El flag --rm asegura que el contenedor se elimina automáticamente después de que se complete su ejecución.


### Ejecutar con Docker Compose:

En la línea de comandos, navega hasta el directorio donde guardaste estos archivos.

Ejecuta el siguiente comando para construir la imagen y ejecutar el contenedor usando Docker Compose:

```sh
docker-compose up --build
```

Esto ejecutará urlf4ck3r y generará el archivo output.txt en el directorio ./output de tu máquina local.

