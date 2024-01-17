#!/usr/bin/env python3
"""
La librería multiprocessing permite crear procesos en Python. 
Cada proceso tiene su propio espacio de memoria, por lo que no comparten 
variables. 
Para comunicar procesos se utilizan tuberías (pipes) o colas (queues). 
La librería multiprocessing también permite crear hilos (threads) con la clase 
Thread. Los hilos son procesos ligeros que comparten memoria y recursos. 
Los hilos se utilizan para ejecutar tareas en paralelo. 
En este ejemplo se crean dos hilos que ejecutan la misma tarea. 
La función time.sleep() se utiliza para simular una tarea que tarda un tiempo en 
ejecutarse. La función join() se utiliza para esperar a que los hilos terminen. 
La función join() bloquea el hilo principal hasta que los hilos terminan. 
La función is_alive() se utiliza para comprobar si un hilo está en ejecución. 
La función enumerate() se utiliza para obtener una lista de los hilos en 
ejecución. 
La función active_count() se utiliza para obtener el número de hilos en 
ejecución.

"""

import multiprocessing
import time


def tarea(num_tarea):

    print(f"\n[+] Proceso {num_tarea} iniciada")

    time.sleep(2)

    print(f"\n[+] Proceso {num_tarea} finalizada")


proceso1 = multiprocessing.Process(target=tarea, args=(1,))
proceso2 = multiprocessing.Process(target=tarea, args=(2,))

proceso1.start()
proceso2.start()

proceso1.join()
proceso2.join()

print(f"\n[+] Los procesos han finalizado")
