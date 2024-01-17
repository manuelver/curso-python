#!/usr/bin/env python3
"""
La librería threading nos permite crear hilos de ejecución en Python.
Un hilo es un flujo de ejecución separado que puede ejecutar código 
simultáneamente con otros hilos de ejecución de nuestro programa.

Los hilos nos permiten ejecutar código concurrente en nuestro programa.

Es importante tener en cuenta que el uso de hilos puede introducir problemas de 
concurrencia, como condiciones de carrera, por lo que debes tener cuidado al 
manipular datos compartidos entre hilos. 

"""

import threading
import time


def tarea(num_tarea):

    print(f"\n[+] Hilo {num_tarea} iniciada")

    time.sleep(2)

    print(f"\n[+] Hilo {num_tarea} finalizada")

# Configurar los hilos
thread1 = threading.Thread(target=tarea, args=(1,))
thread2 = threading.Thread(target=tarea, args=(2,))

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que los hilos terminen
thread1.join()
thread2.join()

print(f"\n[+] Los hilos han finalizado con éxito")
