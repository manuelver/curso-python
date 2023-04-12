"""
Crear y escribir archivos

Sintaxis:
mi_archivo = open('archivo.txt',modo_apetura)
Argumentos de open()
r - Solo lectura - Por defecto
w - Solo escritura. Si el archivo ya existe se resetea
a - Añadir excritura, se posiciona al final.
x - Creación

2 Métodos de escritura
write() Para escribir normal
writelines Para añadir texto en lista
"""

mi_archivo = open('prueba.txt', 'w')
mi_archivo.write('\nEste texto se escribe desde python\n')
mi_archivo.writelines(['Hola', 'mundo', 'aquí', 'estoy'])

mi_archivo.close()
