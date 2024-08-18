
# 🦙 Ollama Telegram Bot

> Repo original: https://github.com/ruecat/ollama-telegram/tree/main

## Prerrequisitos
- [Token de Telegram-Bot](https://core.telegram.org/bots#6-botfather)

## Instalación (Sin Docker)
+ Instala la última versión de [Python](https://python.org/downloads)
+ Clona el repositorio
    ```
    git clone https://github.com/ruecat/ollama-telegram
    ```
+ Instala los requisitos desde requirements.txt
    ```
    pip install -r requirements.txt
    ```
+ Ingresa todos los valores en .env.example

+ Renombra .env.example a .env

+ Inicia el bot

    ```
    python3 run.py
    ```
## Instalación (Imagen Docker)
La imagen oficial está disponible en dockerhub: [ruecat/ollama-telegram](https://hub.docker.com/r/ruecat/ollama-telegram)

+ Descarga el archivo [.env.example](https://github.com/ruecat/ollama-telegram/blob/main/.env.example), renómbralo a .env y completa las variables.
+ Crea un archivo `docker-compose.yml` (opcional: descomenta la parte de GPU en el archivo para habilitar la GPU de Nvidia)

    ```yml
    version: '3.8'
    services:
      ollama-telegram:
        image: ruecat/ollama-telegram
        container_name: ollama-telegram
        restart: on-failure
        env_file:
          - ./.env
      
      ollama-server:
        image: ollama/ollama:latest
        container_name: ollama-server
        volumes:
          - ./ollama:/root/.ollama
        
        # Descomenta para habilitar la GPU de NVIDIA
        # De lo contrario, se ejecuta solo en la CPU:
    
        # deploy:
        #   resources:
        #     reservations:
        #       devices:
        #         - driver: nvidia
        #           count: all
        #           capabilities: [gpu]
    
        restart: always
        ports:
          - '11434:11434'
    ```

+ Inicia los contenedores

    ```sh
    docker compose up -d
    ```

## Instalación (Construye tu propia imagen Docker)
+ Clona el repositorio
    ```
    git clone https://github.com/ruecat/ollama-telegram
    ```

+ Ingresa todos los valores en .env.example

+ Renombra .env.example a .env

+ Ejecuta UNO de los siguientes comandos de docker compose para iniciar:
    1. Para ejecutar ollama en un contenedor de docker (opcional: descomenta la parte de GPU en el archivo docker-compose.yml para habilitar la GPU de Nvidia)
        ```
        docker compose up --build -d
        ```

    2. Para ejecutar ollama desde una instancia instalada localmente (principalmente para **MacOS**, ya que la imagen de docker aún no soporta la aceleración de GPU de Apple):
        ```
        docker compose up --build -d ollama-telegram
        ```

## Configuración del Entorno
|          Parámetro           |                                                        Descripción                                                       | ¿Requerido? | Valor por Defecto |                          Ejemplo                          |
|:----------------------------:|:------------------------------------------------------------------------------------------------------------------------:|:-----------:|:-----------------:|:---------------------------------------------------------:|
|           `TOKEN`            | Tu **token de bot de Telegram**.<br/>[[¿Cómo obtener el token?]](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) |     Sí      |    `yourtoken`    |               MTA0M****.GY5L5F.****g*****5k               |
|         `ADMIN_IDS`          |                       IDs de usuarios de Telegram de los administradores.<br/>Pueden cambiar el modelo y controlar el bot.                      |     Sí      |                   | 1234567890<br/>**O**<br/>1234567890,0987654321, etc.      |
|         `USER_IDS`           |                       IDs de usuarios de Telegram de los usuarios regulares.<br/>Solo pueden chatear con el bot.                        |     Sí      |                   | 1234567890<br/>**O**<br/>1234567890,0987654321, etc.      |
|         `INITMODEL`          |                                                        LLM predeterminado                                                        |     No      |     `llama2`      |           mistral:latest<br/>mistral:7b-instruct          |
|      `OLLAMA_BASE_URL`       |                                                      Tu URL de OllamaAPI                                                       |     No      |                   |            localhost<br/>host.docker.internal             |
|        `OLLAMA_PORT`         |                                                      Tu puerto de OllamaAPI                                                    |     No      |      11434        |                                                             |
|            `TIMEOUT`         |                                El tiempo de espera en segundos para generar respuestas                                        |     No      |       3000        |                                                             |
| `ALLOW_ALL_USERS_IN_GROUPS`  |                   Permite que todos los usuarios en chats grupales interactúen con el bot sin agregarlos a la lista USER_IDS                   |     No      |         0         |                                                             |

## Créditos
+ [Ollama](https://github.com/jmorganca/ollama)

## Librerías utilizadas
+ [Aiogram 3.x](https://github.com/aiogram/aiogram)

