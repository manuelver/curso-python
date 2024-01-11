#!/usr/bin/env python3

import os
from gestor_notas import GestorNotas


def main():

    gestor = GestorNotas()

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"---------------\nMENÚ PRINCIPAL\n---------------")
        print(f"1. Crear nota")
        print(f"2. Leer todas las notas")
        print(f"3. Buscar por una nota")
        print(f"4. Eliminar una nota")
        print(f"5. Salir")

        opcion = input("\n Elige una opción: ")

        if opcion == "1":
            print(f"\n[+] Crear nota\n")
            titulo = input("Título: ")
            contenido = input("Contenido: ")
            gestor.agregar_nota(titulo, contenido)

        elif opcion == "2":
            print(f"\n[i] Mostrando todas las notas\n")
            notas = gestor.leer_notas()

        elif opcion == "3":
            texto_busqueda = input(" Ingresa texto a buscar: ")
            nota = gestor.buscar_nota(texto_busqueda)

        elif opcion == "4":

            try:

                index = int(input(" Introducir índice de la nota a eliminar: "))
                gestor.eliminar_nota(index)

            except ValueError:

                print(f"\n[!] Error: Opción no válida.\n")

        elif opcion == "5":
            print(f"\n[!] Saliendo... ¡Hasta pronto!\n")
            break

        else:
            print(f"\n[!] Error: Opción no válida\n")

        input(f"\n[+] Pulsa <ENTER> para continuar...\n")


if __name__ == "__main__":
    main()
