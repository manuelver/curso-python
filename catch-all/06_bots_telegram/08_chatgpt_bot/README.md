
# ChatGPT Telegram Bot: **GPT-4. Rápido. Sin límites diarios. Modos de chat especiales**

> Repositorio original: https://github.com/father-bot/chatgpt_telegram_bot

Este repositorio es ChatGPT recreado como un Bot de Telegram.

Puedes desplegarlo tu mismo.

## Características

- Respuestas con baja latencia (usualmente toma entre 3-5 segundos)
- Sin límites de solicitudes
- Transmisión de mensajes (mira la demo)
- Soporte para GPT-4 y GPT-4 Turbo
- Soporte para GPT-4 Vision
- Soporte para chat en grupo (/help_group_chat para obtener instrucciones)
- DALLE 2 (elige el modo 👩‍🎨 Artista para generar imágenes)
- Reconocimiento de mensajes de voz
- Resaltado de código
- 15 modos de chat especiales: 👩🏼‍🎓 Asistente, 👩🏼‍💻 Asistente de Código, 👩‍🎨 Artista, 🧠 Psicólogo, 🚀 Elon Musk, entre otros. Puedes crear fácilmente tus propios modos de chat editando `config/chat_modes.yml`
- Soporte para [ChatGPT API](https://platform.openai.com/docs/guides/chat/introduction)
- Lista de usuarios de Telegram permitidos
- Seguimiento del balance $ gastado en la API de OpenAI

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmM2ZWVjY2M4NWQ3ZThkYmQ3MDhmMTEzZGUwOGFmOThlMDIzZGM4YiZjdD1n/unx907h7GSiLAugzVX/giphy.gif" />
</p>

---

## Comandos del Bot

- `/retry` – Regenerar la última respuesta del bot
- `/new` – Iniciar nuevo diálogo
- `/mode` – Seleccionar modo de chat
- `/balance` – Mostrar balance
- `/settings` – Mostrar configuraciones
- `/help` – Mostrar ayuda

## Configuración

1. Obtén tu clave de [OpenAI API](https://openai.com/api/)

2. Obtén tu token de bot de Telegram desde [@BotFather](https://t.me/BotFather)

3. Edita `config/config.example.yml` para establecer tus tokens y ejecuta los 2 comandos a continuación (*si eres un usuario avanzado, también puedes editar* `config/config.example.env`):
    ```bash
    mv config/config.example.yml config/config.yml
    mv config/config.example.env config/config.env
    ```

4. 🔥 Y ahora **ejecuta**:
    ```bash
    docker-compose --env-file config/config.env up --build
    ```

## Referencias

1. [*Construye ChatGPT desde GPT-3*](https://learnprompting.org/docs/applied_prompting/build_chatgpt)
