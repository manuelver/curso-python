#!/usr/bin/env python3

class Nota:

    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def __str__(self):
        return f"""
    Título: {self.titulo.upper()}
    {self.contenido}
    """
