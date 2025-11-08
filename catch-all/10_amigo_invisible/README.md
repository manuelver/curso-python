# README - Amigo Invisible (Secret Santa)

Este es un script en Python diseñado para organizar un intercambio de regalos de "Amigo Invisible" de manera automática. Permite generar asignaciones de personas de forma aleatoria, asegurándose de que no haya emparejamientos invalidos, como asignar a alguien a sí mismo o asignar a alguien con exclusiones especificadas.

Además, si se habilita la opción de enviar correos electrónicos, el script enviará un correo a cada participante notificándole a quién le ha tocado regalar, usando plantillas personalizables.

## Requisitos

* Python 3.x
* Paquetes de Python requeridos:

  * `csv`
  * `random`
  * `argparse`
  * `smtplib`
  * `os`
  * `logging`
  * `email`
  * `dotenv`

Puedes instalar las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install python-dotenv
```

Si usas un entorno virtual, asegúrate de activarlo antes de instalar las dependencias.

## Descripción de Funcionalidades

### Entradas

El script toma como entrada un archivo CSV que contiene la lista de participantes. El archivo CSV debe tener las siguientes columnas:

* `name`: Nombre del participante.
* `email`: Correo electrónico del participante.
* `exclusions`: (Opcional) Lista de participantes a los que **no** pueden ser asignados como "Amigo Invisible". Los valores deben estar separados por punto y coma.

Ejemplo de archivo CSV `participants.csv`:

```csv
name,email,exclusions
Juan,juan@example.com,
María,maria@example.com,juan@example.com
Pedro,pedro@example.com,juan@example.com
```

En el caso de que un participante no tenga exclusiones, se deja en blanco la columna `exclusions`.

### Opciones del Script

Este es el uso básico del script:

```bash
python secret_santa.py --input participants.csv
```

#### Opciones disponibles:

* `--input PATH`
  Ruta al archivo CSV de entrada (por defecto `participants.csv`).

* `--output PATH`
  Ruta al archivo CSV de salida donde se guardarán las asignaciones (por defecto `assignments.csv`).

* `--seed INT`
  Semilla para la generación aleatoria. Esto permite hacer el proceso reproducible.

* `--send`
  Habilita el envío de correos electrónicos. Si no se incluye, los correos no se enviarán.

* `--smtp-server HOST`
  Servidor SMTP para el envío de correos (por defecto, `smtp.gmail.com`).

* `--smtp-port PORT`
  Puerto SMTP (por defecto, 587).

* `--smtp-user USER`
  Usuario SMTP (requiere autenticación).

* `--smtp-pass PASS`
  Contraseña SMTP. **Es recomendable utilizar una variable de entorno en lugar de escribir la contraseña directamente.**

* `--subject-template`
  Ruta al archivo de plantilla del asunto del correo.

* `--body-template`
  Ruta al archivo de plantilla del cuerpo del correo.

* `--max-attempts N`
  Número máximo de intentos para generar emparejamientos aleatorios (por defecto, 10000).

## Flujo de Trabajo

1. **Leer Participantes:**
   El script lee el archivo `participants.csv` y extrae los datos de los participantes, incluyendo sus exclusiones.

2. **Generación de Asignaciones:**
   Se genera un emparejamiento aleatorio entre los participantes. El script se asegura de que:

   * Un participante no se empareje con sí mismo.
   * Un participante no sea asignado a una persona de su lista de exclusiones.

   Si no se puede encontrar una asignación válida después de varios intentos (por defecto, 10000), el script usa un algoritmo de **backtracking** para intentar encontrar una solución.

3. **Guardar Asignaciones:**
   Las asignaciones generadas se guardan en un archivo CSV con el formato:

   ```csv
   giver_name,giver_email,recipient_name,recipient_email
   ```

4. **Enviar Correos Electrónicos (Opcional):**
   Si se habilita la opción `--send`, el script enviará un correo electrónico a cada participante notificándole a quién le ha tocado regalar.

   Los correos electrónicos usan plantillas personalizables para el asunto y el cuerpo del mensaje. Puedes crear estos archivos como plantillas y proporcionarlas al script a través de los parámetros `--subject-template` y `--body-template`.

### Estructura de Archivos

La estructura recomendada para el proyecto es la siguiente:

```
.
├── secret_santa.py         # Script principal
├── .env                    # Variables de entorno (por ejemplo, SMTP credentials)
├── participants.csv        # Lista de participantes
├── assignments.csv         # Archivo generado con las asignaciones
├── templates/
│   ├── subject.txt         # Plantilla de asunto para los correos
│   └── body.txt            # Plantilla de cuerpo para los correos
└── secret_santa.log        # Archivo de registro (log)
```

#### Archivos `.env`

El archivo `.env` debe contener las variables necesarias para la autenticación SMTP. Este archivo **no debe ser subido a repositorios públicos** (asegúrate de que esté en el archivo `.gitignore`). Un ejemplo de `.env` podría ser:

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tu_correo@gmail.com
SMTP_PASS=tu_contraseña
LOG_LEVEL=INFO
```

#### Plantillas de Correo

Las plantillas para el **asunto** y el **cuerpo** del correo se deben almacenar en archivos de texto en la carpeta `templates/`. Estos archivos pueden contener variables que se reemplazarán dinámicamente con los datos de cada participante.

Ejemplo de archivo `templates/subject.txt`:

```
¡Tu Amigo Invisible es {recipient_name}!
```

Ejemplo de archivo `templates/body.txt`:

```
¡Hola {giver_name}!

Te ha tocado regalar a {recipient_name}, cuyo correo es {recipient_email}.

¡Suerte con la compra de tu regalo!

Atentamente,
El equipo de Amigo Invisible
```

## Uso

### Ejemplo Básico

Si quieres realizar el emparejamiento sin enviar correos electrónicos:

```bash
python secret_santa.py --input participants.csv --output assignments.csv
```

### Ejemplo con Correos

Si deseas enviar correos electrónicos a los participantes, usa la opción `--send`:

```bash
python secret_santa.py --input participants.csv --output assignments.csv --send --smtp-user "tu_correo@gmail.com" --smtp-pass "tu_contraseña"
```

### Personalización de Plantillas

Si prefieres personalizar el asunto y el cuerpo de los correos, puedes hacerlo editando los archivos de plantilla:

* `templates/subject.txt`
* `templates/body.txt`

Luego, solo necesitas especificar las rutas a estos archivos con las opciones `--subject-template` y `--body-template` al ejecutar el script.

## Registros

El script genera un archivo de log llamado `secret_santa.log`, donde se registran todas las actividades realizadas. Puedes revisar este archivo para obtener detalles sobre el proceso de asignación, cualquier error o advertencia, y las actividades de envío de correos.

## Excepciones y Errores

El script maneja diversas excepciones, como errores de lectura de archivo CSV, errores al enviar correos electrónicos, o si no se encuentran suficientes participantes.

Si un error ocurre, el script terminará su ejecución con un mensaje de error detallado.

## Contribuciones

Si deseas realizar mejoras o reportar problemas, por favor abre un **Issue** o envía un **Pull Request**. ¡Cualquier contribución será bienvenida!

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

Este `README` proporciona una guía completa para el uso de este script, la configuración de los parámetros y el manejo de excepciones. Si tienes más dudas o necesitas personalizar algún aspecto del script, no dudes en preguntarme. ¡Feliz organización de tu Amigo Invisible! 🎁
