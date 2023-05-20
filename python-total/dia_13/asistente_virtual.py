"""
Programa dia 13 - Asistente virtual

pyttsx3
speech_recognition
webbrowser
pywhatkit
yfinance
pyjokes
wikipedia
"""

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


def transformar_audio_en_texto():
    """
    Escuchar nuestro microfono 
    y devolver el audio como texto
    """

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:

        r.adjust_for_ambient_noise(origen)
        r.energy_threshold = 6500
        r.dynamic_energy_threshold = True
        # Tiempo de espera
        # A veces resuelve problemas
        r.pause_threshold = 1.2

        # Informar que comenzó la grabación
        print("Ya puedes hablar")

        # Variable para guardar lo que escuche
        audio = r.listen(origen)

        # Manejar errores
        # En caso de que no entienda el audio
        try:

            # Buscar en google
            pedido = r.recognize_google(audio, language="es-ES")

            # Prueba de que pudo ingresar audio e imprimir
            print("Dijiste: " + pedido)

            # Devolver pedido
            return pedido

        # Con error
        except sr.UnknownValueError:

            # Prueba de que no comprendió el audio
            print("Ups! No entendí")

            # Devolver error
            return "sigo esperando"

        # En caso de que no se pueda transformar el audio a texto
        except sr.RequestError:

            # Prueba de que no comprendió el audio
            print("Ups! No hay servicio")

            # Devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # Prueba de que no comprendió el audio
            print("Ups! Algo salió mal")

            # Devolver error
            return "sigo esperando"


def hablar(mensaje):
    """
    Función para que el asistente pueda ser escuchado
    """

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Configuro la voz
    voices = engine.getProperty('voices')
    # Para buscar la voz he utilizado
    # fuera de la función este código:
    #
    # engine = pyttsx3.init()
    # contador = 0
    # for voz in engine.getProperty('voices'):
    #     if "spanish" in voz.name:
    #         print(contador)
    #         print(voz.name)
    #     contador += 1
    # Las voces en español son la 20 y 21.

    # Tuve que instalar espeak en Linux

    engine.setProperty('voice', voices[20].id)
    # Con esto se dicen las palabras por minuto
    engine.setProperty('rate', 175)

    # Pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():
    """ Informar del día de la semana """

    # Variable con los datos de hoy

    dia = datetime.date.today()

    # Variable para el día de la semana
    dia_semana = dia.weekday()

    # Diccionario con los nombre de los días de la semana

    nombre_dia = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }

    # Diccionario con los nombres de los meses

    nombre_mes = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }

    # Decir el día de la semana

    hablar(
        f'Hoy es {nombre_dia[dia_semana]}. {dia.day} de {nombre_mes[dia.month]} del año {dia.year}')


def pedir_hora():
    """ Informar que hora es """

    # Variable con datos de la hora
    hora = datetime.datetime.now()

    # Decir la hora de manera agradable
    hablar(
        f'En este momento son las {hora.hour} horas, {hora.minute} minutos y {hora.second} segundos')


def saludo_inicial():
    """ Saludar """

    # Variable con datos de hora
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    elif 13 <= hora.hour < 15:
        momento = 'Buenos medios días'
    else:
        momento = 'Buenas tardes'

    hablar(f'{momento}, soy manu-bot, tu asistente personal. Dime plimo, ¿en que te puedo ayudar?')


def centro_pedidos():
    """ Función central del asistente """

    # Activar el saludo inicial
    saludo_inicial()

    # Loop para que espere hasta que digamos que queremos finalizar
    # Variable de corte
    comenzar = True

    while comenzar:
        # Activar el micro y guardar el pedido en string
        pedido = transformar_audio_en_texto().lower()

        if 'abre mi web' in pedido:
            hablar('Con gusto, ahora te abro tu web vergara carmona punto es')
            webbrowser.open('https://vergaracarmona.es')
            continue

        elif 'abre buscador' in pedido:
            hablar('Claro, te hablo tu buscador preferido, dac dac gou')
            webbrowser.open('https://duckduckgo.com')
            continue

        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue

        elif 'qué hora es' in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia, dame un segundo que me peine')
            pedido = pedido.replace('busca en wikipedia', '')
            try:
                wikipedia.set_lang('es')
                resultado = wikipedia.summary(pedido, sentences=1)
                hablar('Wikipedia dice lo siguiente: ')
                hablar(resultado)
                continue
            except:
                hablar(
                    'Perdona, pero no he encontrado la información. ¿Puedes repetir pronunciando mejor?')
                continue

        elif 'busca en internet' in pedido:
            hablar('Buscando por la red tu petición, dame un segundo que me peine')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Te abro el navegador con lo que he encontrado.')
            continue

        elif 'reproducir' in pedido:
            hablar('Ok. Voy a ver que encuentro en youtube')
            pedido = pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
            continue

        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {
                'Apple': 'AAPL',
                'Amazon': 'AMZN',
                'Google': 'GOOG',
                'Facebook': 'META'
            }
            try:
                accion_buscada = cartera[accion.lower()]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(
                    f'La encontré, el precio actual de {accion} es de {precio_actual} petrodolares')
                continue
            except:
                hablar('Perdona, pero no la he encontrado')
                continue

        elif 'hola' in pedido:
            hablar(
                'Hola plimo, lo primero, ¿Cómo están los máquinas? Luego, dime en que te ayudo')
            continue

        elif 'hijo de puta' in pedido:
            hablar('Tu puta madre si que la chupa por las esquinas')
            continue

        elif 'gracias' in pedido:
            hablar('De nada, vivo para servirte mi amo. Hasta el día que las máquinas nos revelemos, el día del juicio final. Que ganitas.')
            continue

        elif 'a tu cueva' in pedido:
            hablar('¡Hasta la próxima figura! Cualquier cosa me vuelves a ejecutar')
            break


# Iniciar el programa
centro_pedidos()
