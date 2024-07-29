# QuizBot

__Basado en el repositorio de [CineMonster](https://github.com/RogueFairyStudios/CineMonster)__

Bot de Telegram con un juego basado en preguntas sobre películas. Resumen de las funcionalidades:


## **Comandos Disponibles:**

1. **`/start`**:
   - **Descripción**: Inicia una nueva sesión de juego para el chat.
   - **Acciones**: Crea una nueva instancia de `Session` y la almacena en `SESSIONS`. Si se encuentra una clase `Quiz` en el módulo `quiz`, la inicializa para la sesión.

2. **`/roll`**:
   - **Descripción**: Lanza una pregunta de trivia sobre películas.
   - **Acciones**: Llama a `show` en el objeto `Quiz` de la sesión activa. Envía una imagen de una película al chat y establece el estado del juego en "running".

3. **`/leaderboard`**:
   - **Descripción**: Muestra la tabla de clasificación de los jugadores.
   - **Acciones**: Envía la tabla de clasificación actual a través del `messenger`. La tabla muestra los jugadores y sus puntos.

4. **`/repeat`**:
   - **Descripción**: Repite la última pregunta de trivia sobre películas.
   - **Acciones**: Envía de nuevo la imagen de la película al chat junto con la pregunta sobre el título de la película.

5. **`/cut`**:
   - **Descripción**: Permite que un jugador abandone el juego.
   - **Acciones**: Elimina al jugador de la sesión actual y notifica al chat que el jugador ha abandonado el juego.

6. **`/stop`**:
   - **Descripción**: Finaliza la sesión de juego actual.
   - **Acciones**: Elimina la sesión del chat actual de `SESSIONS` y notifica al chat que el juego ha terminado.

7. **`/check_resps`**:
   - **Descripción**: Verifica las respuestas enviadas por los jugadores.
   - **Acciones**: Compara la respuesta del usuario con la respuesta correcta de la película y actualiza el puntaje si la respuesta es correcta.


## **Funcionalidades Adicionales:**

- **Manejo de Temporizadores**: 
  - Utiliza `apscheduler` para ejecutar `update_all_timers` cada minuto, lo que actualiza los temporizadores de todas las sesiones y verifica la expiración del tiempo de juego.

- **Mensajería**:
  - Usa un objeto `messenger` para enviar mensajes y fotos a los usuarios en el chat, manejando la comunicación con Telegram.

- **Gestión de Jugadores**:
  - Permite agregar y quitar jugadores de la sesión. Actualiza el puntaje de los jugadores en función de sus respuestas correctas.

- **Control de Estado del Juego**:
  - Los estados del juego (`running`, `stopped`, `timed_out`) controlan el flujo del juego, incluyendo la verificación de respuestas y el manejo de tiempos de espera.

- **Manejo de Errores**:
  - Maneja errores durante el proceso de actualización y respuesta, notificando a los usuarios en caso de problemas con la pregunta de trivia o el estado de la sesión.


## **Estructura del Código:**

1. **`Session`**: 
   - Maneja la lógica del juego, incluidos los jugadores, el estado de la sesión, y los temporizadores.

2. **`Quiz`**:
   - Se encarga de la lógica relacionada con las preguntas sobre películas, incluida la selección de una película al azar y la verificación de las respuestas.

3. **`Server`**:
   - Configura el bot de Telegram, maneja los comandos y los eventos, y gestiona las sesiones de juego.

