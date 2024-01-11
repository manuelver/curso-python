#!/usr/bin/env python3

import pickle
from notas import Nota


class GestorNotas:

    def __init__(self, archivo_notas='notas.pkl'):

        self.archivo_notas = archivo_notas

        try:

            with open(self.archivo_notas, 'rb') as f:

                self.notas = pickle.load(f)

        except FileNotFoundError:

            self.notas = []

    def guardar_notas(self):

        with open(self.archivo_notas, 'wb') as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self, titulo, contenido):

        self.notas.append(Nota(titulo, contenido))
        self.guardar_notas()

    def leer_notas(self):
        for i, nota in enumerate(self.notas):
            print(f"- NOTA {i+1}: {nota}")

    def buscar_nota(self, texto_busqueda):

        notas_encontradas = []

        for nota in self.notas:

            if texto_busqueda in nota.titulo or texto_busqueda in nota.contenido:

                notas_encontradas.append(nota)

        if notas_encontradas:

            print(f"\n[i] Resultado de la búsqueda\n")

            for i, nota in enumerate(notas_encontradas):

                print(f"- RESULTADO {i+1}: {nota}")

            notas_encontradas.clear()

        else:

            print(f"\n[!] No se encontraron resultados\n")

    def eliminar_nota(self, index):

        # if index >= 1 or index <= len(self.notas):

        try:
            index_a_borrar = int(index - 1)
            print(
                f"\n[+] Eliminando nota {index}: {self.notas[index_a_borrar]}")
            del self.notas[index_a_borrar]
            self.guardar_notas()

        except IndexError:

            print(f"\n[!] Error: No existe la nota\n")
