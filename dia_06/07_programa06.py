"""
Programa día 6 - Recetario
"""
import os
import shutil
from pathlib import Path

"""
Variables
"""
ruta_base = Path('Recetas')
limpiar = 'clear'
sleep = 'sleep 2'

"""
Funciones
"""


def clearConsole():
    # Función limpiar consola
    os.system(limpiar)


def bienvenida():
    clearConsole()
    # bienvenida al usuario
    print('\n', '#' * 29, '\n #  Bienvenid@ al Recetario  #\n', '#' * 29)
    os.system(sleep)
    clearConsole()
    info()


def info():

    # informar la ruta de acceso al directorio donde se encuentran las recetas
    print('*' * 17, '\n*  INFORMACIÓN  *\n*****************\n')
    print('Las recetas están en las siguientes rutas:')

    for ruta in Path(ruta_base).glob('*'):
        print(f'- {ruta}')

    # informar cuántas recetas hay en total dentro de esas carpetas
    num_recetas = 0
    for ruta in Path(ruta_base).glob('**/*.txt'):
        num_recetas += 1

    # Mostra menú de opciones
    print(f'\nEn total, existen {num_recetas} recetas.\n')
    menu_opciones()


def menu_opciones():

    comando = ''
    while comando.lower() != 's':
        print("""********************
*  MENÚ PRINCIPAL  *
********************

    i\t\tInformación
    m\t\tMostrar recetas
    cr\t\tCrear receta
    cc\t\tCrear nueva categoria
    er\t\tEliminar receta
    ec\t\tEliminar categoria
    s\t\tsalir
    """)

        comando = input('Selecciona una opción: ')
        clearConsole()

        if comando == 'i':
            # Información
            info()
        elif comando == 'm':
            com = ""
            while com != 's':
                # Mostrar recetas
                cat = escoger_categoria()
                rec = escoger_receta(cat)
                mostrar_receta(rec)

                com = input("¿Quieres salir de \"Mostrar recetas\"? (s/n) ")
                if com == 'n':
                    continue
                elif com == 's':
                    print('\n¡Ok! Volvemos al menú pricipal\n')
                    break
                else:
                    print('Disculpa, ingresa un valor válido')
                    continue

        elif comando == 'cr':
            com = ""
            while com != 's':
                # Crear receta
                cat = escoger_categoria()
                crear_receta(cat)

                com = input("¿Quieres salir de \"Crear receta\"? (s/n) ")
                if com == 'n':
                    continue
                elif com == 's':
                    print('\n¡Ok! Volvemos al menú pricipal\n')
                    break
                else:
                    print('Disculpa, ingresa un valor válido')
                    continue

        elif comando == 'cc':

            # Crear nueva categoria
            crear_categoria()

        elif comando == 'er':
            com = ""
            while com != 's':
                # Eliminar receta
                cat = escoger_categoria()
                rec = escoger_receta(cat)
                eliminar_receta(rec)

                com = input("¿Quieres salir de \"eliminar receta\"? (s/n) ")
                if com == 'n':
                    continue
                elif com == 's':
                    print('\n¡Ok! Volvemos al menú pricipal\n')
                    break
                else:
                    print('Disculpa, ingresa un valor válido')
                    continue

        elif comando == 'ec':
            com = ""
            while com != 's':
                # Eliminar categoria
                cat = escoger_categoria()
                eliminar_categoria(cat)

                com = input("¿Quieres salir de \"eliminar categoria\"? (s/n) ")
                if com == 'n':
                    continue
                elif com == 's':
                    print('\n¡Ok! Volvemos al menú pricipal\n')
                    break
                else:
                    print('Disculpa, ingresa un valor válido')
                    continue

        elif comando == 's':
            # salir
            break
        else:
            print('Disculpa, ingresa un valor válido')
            os.system(sleep)
            clearConsole()
            info()


def escoger_categoria():
    # Opción 1
    # Pregunta qué categoría elige (carnes, ensaladas, etc.),
    print('\nCategorías:')

    num_menu = 0
    lista_categorias = []
    for ruta in Path(ruta_base).glob('*'):
        num_menu += 1
        lista_categorias.append(ruta.name)
        print(f'\t{num_menu}\t {lista_categorias[num_menu - 1]}')
    print('\n\ts\t salir de la opción \"escoger categoria\"\n')

    opcion = ''
    while opcion != 's':
        opcion = input('Escoger categoria: ')

        if opcion.isnumeric():

            if int(opcion) in range(1, num_menu + 1):
                categoria = lista_categorias[int(opcion) - 1]
                return categoria

            else:
                print(f'\nEl número {opcion} no está en el menú\n')
                continue
        elif opcion.lower() == 's':
            return False
        else:
            print('Disculpa, ingresa un valor válido')
            continue
    return False


def escoger_receta(catego):

    if catego == False:
        return False
    else:
        # una vez que el usuario elija una, preguntar qué receta quiere leer,
        print(
            f'\nEn la categoria \"{catego.upper()}\" hay las siguientes recetas: ')

        num_menu = 0
        lista_recetas = []
        for rut in Path(ruta_base, catego).glob('*'):
            num_menu += 1
            lista_recetas.append(rut.name)
            print(f'\t{num_menu}\t {lista_recetas[num_menu - 1]}')
        print('\n\ts\t salir de la opción \"escoger receta\"\n')

        opcion = ''
        while opcion != 's':
            opcion = input('Escoger receta: ')

            if opcion.isnumeric():

                if int(opcion) in range(1, num_menu + 1):
                    receta = lista_recetas[int(opcion) - 1]
                    ruta_escogida = Path(ruta_base, catego, receta)
                    # Devuelve receta escogida
                    return ruta_escogida

                else:
                    print(f'\nEl número {opcion} no está en el menú\n')
                    continue
            elif opcion.lower() == 's':
                return False
            else:
                print('Disculpa, ingresa un valor válido')
                continue


def mostrar_receta(ruta_escogida):

    # mostrar contenido receta.
    if ruta_escogida == False:
        print()

    else:
        clearConsole()
        print(
            f'\nRECETA \"{ruta_escogida.stem.upper()}\"\n{ruta_escogida.read_text()}\n')


def crear_receta(categoria):
    # Opción 2
    # Elegir una categoría,
    # va a pedir que escriba el nombre y el contenido de la nueva receta que quiere crear,
    # El programa va a crear ese archivo en el lugar correcto.
    if categoria == False:
        print()

    else:
        catego = Path(ruta_base, categoria)

        nombre = input('¿Cómo le quieres llamar a la receta? ')

        nueva_receta = nombre + ".txt"

        os.chdir(catego)
        receta = open(nueva_receta.capitalize(), 'x')
        receta.close()

        nuevo_texto = open(nueva_receta.capitalize(), 'w')
        nuevo_texto.write(input('Escribe el contenido de la receta: '))
        nuevo_texto.close()

        os.chdir('../..')

        print(f'\nReceta de \"{nombre}\" creada con éxito\n')


def crear_categoria():
    # Opcion 3
    # Preguntar el nombre de la categoría que quiere crear
    # Generar una carpeta nueva con ese nombre.
    nueva_categ = input('¿Cómo quieres llamar la nueva categoria? ')
    catego = Path(ruta_base, nueva_categ.capitalize())
    os.makedirs(catego)

    print(f'\nCategoria \"{nueva_categ}\" creada con éxito.\n')


def eliminar_receta(ruta_escogida):
    # Opción 4
    # hará lo mismo que la opción uno,
    # pero en vez de leer la receta, la va a eliminar.
    if ruta_escogida == False:
        print()

    else:
        print(
            f'Se ha eliminado la RECETA \"{ruta_escogida.stem.upper()}\"\n')
        os.remove(ruta_escogida)


def eliminar_categoria(categoria):
    # Opción 5
    # Preguntar qué categoría quiere eliminar
    # Eliminar categoria
    if categoria == False:
        print()

    else:
        catego = Path(ruta_base, categoria)
        print(
            f'Se ha eliminado la CATEGORIA \"{catego.stem.upper()}\"\n')
        shutil.rmtree(catego)


"""
El programa se dispara en la función bienvenida
"""

bienvenida()

print('\n¡Ciao!\n')
