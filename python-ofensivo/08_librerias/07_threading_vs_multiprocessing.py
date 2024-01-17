#!/usr/bin/env python3
"""
Ejemplo práctico para ver la diferencia entre ejecutar un programa con hilos, con procesos y 
sin ninguno de los anteriores.

"""

import time
import requests
import threading
import multiprocessing

dominios = {
    "https://google.com",
    "https://xvideos.com",
    "https://wikimedia.org",
    "https://yahoo.com"
}

# Ejecución sin hilos ni procesos separados
start_time = time.time()

for url in dominios:

    r = requests.get(url)
    print(
        f"\n[+] URL {url}: {len(r.content)} bytes"
    )


end_time = time.time()

print(
    f"\n[i] Tiempo de ejecución SIN hilos: {end_time - start_time} segundos\n"
)


def realizar_peticion(url):

    r = requests.get(url)
    print(
        f"\n[+] URL {url}: {len(r.content)} bytes"
    )


# Ejecución con hilos
start_time = time.time()

hilos = []
for url in dominios:

    hilo = threading.Thread(
        target=realizar_peticion,
        args=(url,)
    )
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:

    hilo.join()

end_time = time.time()

print(
    f"\n[i] Tiempo de ejecución CON hilos: {end_time - start_time} segundos\n"
)


# Ejecución con procesos
start_time = time.time()

procesos = []
for url in dominios:

    proceso = multiprocessing.Process(
        target=realizar_peticion,
        args=(url,)
    )
    proceso.start()
    procesos.append(proceso)

for proceso in procesos:

    proceso.join()

end_time = time.time()

print(
    f"\n[i] Tiempo de ejecución CON procesos: {end_time - start_time} segundos\n"
)
