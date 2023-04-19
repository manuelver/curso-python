"""
Programa día 12 - Aplicación de facturación - Mi restaurant

tkinter
"""

from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

# Variable calc
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65, 2.70]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58, 1.70]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74, 1.80]


# Funciones


def click_boton(numero):
    """
    Función para extraer string de los botones
    """
    # Hacemos global la variable operador
    global operador

    # Añadir la nueva insercción a la variable operador
    operador = operador + numero

    # Antes de introducir el número se debe borrar lo que guarda
    # del click anterior
    visor_calculadora.delete(0, END)

    # Mostrar en el campo visor lo que contiene la variable operador
    visor_calculadora.insert(END, operador)


def borrar():
    """
    Función para borrar de calculadora a través del botón
    """

    # Hacemos global la variable operador
    # y reseteamos el operador
    global operador
    operador = ''
    # Ahora borramos el contenido del visor
    visor_calculadora.delete(0, END)


def obtener_resultado():
    """
    Mostrar en visor calculadora el resultado de la operación guardada
    """
    global operador
    # Primero evaluamos operador para extraer el resultado,
    # lo metemos en un string y guardamos en nueva variable
    resultado = str(eval(operador))

    # Ahora borramos el contenido del visor
    visor_calculadora.delete(0, END)
    # e introducimos el contenido variable resultado al visor
    visor_calculadora.insert(0, resultado)

    # Por último reseteamos el operador
    operador = ''


def revisar_check():
    """
    Revisará si algún checkbox tiene contenido
    """

    # Checkear comidas
    # Contador de los índices de las listas de checkbox
    x = 0
    # Comprobar cada cuadro comida
    for c in cuadros_comida:
        # Si el checkbox está en True
        if variables_comida[x].get() == 1:
            # Habilitar el cuadro
            cuadros_comida[x].config(state=NORMAL)
            # Eliminar el 0 inicial del visor
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            # Quede el focus en el visor
            cuadros_comida[x].focus()
        # Si el checkbox está en False
        else:
            # Deshabilitar el cuadro
            cuadros_comida[x].config(state=DISABLED)
            # Setear a cero el visor
            texto_comida[x].set('0')

        # Sumarle un valor al contador
        x += 1

    # Checkear bebidas
    # Contador de los índices de las listas de checkbox
    x = 0
    # Comprobar cada cuadro bebida
    for c in cuadros_bebida:
        # Si el checkbox está en True
        if variables_bebida[x].get() == 1:
            # Habilitar el cuadro
            cuadros_bebida[x].config(state=NORMAL)
            # Eliminar el 0 inicial del visor
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            # Quede el focus en el visor
            cuadros_bebida[x].focus()
        # Si el checkbox está en False
        else:
            # Deshabilitar el cuadro
            cuadros_bebida[x].config(state=DISABLED)
            # Setear a cero el visor
            texto_bebida[x].set('0')

        # Sumarle un valor al contador
        x += 1

    # Checkear postres
    # Contador de los índices de las listas de checkbox
    x = 0
    # Comprobar cada cuadro postre
    for c in cuadros_postre:
        # Si el checkbox está en True
        if variables_postre[x].get() == 1:
            # Habilitar el cuadro
            cuadros_postre[x].config(state=NORMAL)
            # Eliminar el 0 inicial del visor
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            # Quede el focus en el visor
            cuadros_postre[x].focus()
        # Si el checkbox está en False
        else:
            # Deshabilitar el cuadro
            cuadros_postre[x].config(state=DISABLED)
            # Setear a cero el visor
            texto_postre[x].set('0')

        # Sumarle un valor al contador
        x += 1


def total():
    """
    Calculos del total de comidas, bebidas y postres seleccionados
    multiplicarlos por el precio de los items
    hacer un subtotal
    calcular los impuestos 
    Total items 
    Total final
    """

    # Comida
    # Variable guardar subtotal
    subtotal_comida = 0
    # Contador indice
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + \
            (float(cantidad.get()) * precios_comida[p])
        p += 1

    # Bebida
    # Variable guardar subtotal
    subtotal_bebida = 0
    # Contador indice
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + \
            (float(cantidad.get()) * precios_bebida[p])
        p += 1

    # Postre
    # Variable guardar subtotal
    subtotal_postre = 0
    # Contador indice
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + \
            (float(cantidad.get()) * precios_postre[p])
        p += 1

    # Guardar en variables calculos de subtotal, impuestos y total
    subtotal = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = subtotal * 0.1
    total = subtotal + impuestos

    # Asignar a las variables de costos los calculos que corresponda
    var_costo_comida.set(f'{round(subtotal_comida, 2)} €')
    var_costo_bebida.set(f'{round(subtotal_bebida, 2)} €')
    var_costo_postre.set(f'{round(subtotal_postre, 2)} €')
    var_subtotal.set(f'{round(subtotal, 2)} €')
    var_impuesto.set(f'{round(impuestos, 2)} €')
    var_total.set(f'{round(total, 2)} €')


def recibo():
    """
    Calcular el recibo con:
    - Número de recibo (random) 
    - Fecha (datetime)
    - todos los elementos seleccionados y su precio
    - Subtotal, impuestos y total
    """
    # Antes de comenzar debemos asegurar que el visor está en blanco
    texto_recibo.delete(1.0, END)

    # Variable núm. recibo
    num_recibo = f'N# - {random.randint(1000, 9999)}'

    # Variable fecha y su formato
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Descripción\t\t\tCant.\tPrecio\n')
    texto_recibo.insert(END, f'-' * 68 + '\n')

    # Contador de registros comida
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(
                END,
                f'{lista_comidas[x]}\t\t\t{comida.get()}\t{int(comida.get()) * precios_comida[x]} €\n'
            )
        x += 1

    # Contador de registros bebida
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(
                END,
                f'{lista_bebidas[x]}\t\t\t{bebida.get()}\t{int(bebida.get()) * precios_bebida[x]} €\n'
            )
        x += 1

    # Contador de registros postre
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(
                END,
                f'{lista_postres[x]}\t\t\t{postre.get()}\t{int(postre.get()) * precios_postre[x]} €\n'
            )
        x += 1

    texto_recibo.insert(END, f'-' * 68 + '\n')
    texto_recibo.insert(
        END, f' Total de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(
        END, f' Total de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(
        END, f' Total de la postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 68 + '\n')
    texto_recibo.insert(
        END, f' Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(
        END, f' Impuestos 10%: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(
        END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, '\tLe esperamos pronto')


def guardar():
    """
    Guardar en un fichero el recibo
    Utilizaremos filedialog, messagebox de tkinter
    """
    # Variable con la información que tenemos en el recibo
    info_recibo = texto_recibo.get(1.0, END)

    # Variable con el archivo del elemento pidiendo que se guarde como archivo
    # Especificamos que escriba y por defecto la extensión
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    # Escribimos en el fichero
    archivo.write(info_recibo)
    archivo.close()

    # Informamos al usuario que se ha guardado
    # con un cuadro de dialogo
    messagebox.showinfo('Información', 'Su recibo se ha guardado')


def resetear():
    """
    Borrar todos los campos
    """

    # Borrar campo recibo
    texto_recibo.delete(0.1, END)

    # Borrar campo comidas, bebidas y postres
    for texto in texto_comida:
        texto.set('0')

    for texto in texto_bebida:
        texto.set('0')

    for texto in texto_postre:
        texto.set('0')

    # Desactivar cuadros visores comidas, bebidas y postres
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    # Desactivar checkbox comidas, bebidas y postres
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    # Desactivar todos los costos
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


"""
Configuración de la aplicación
"""

# Iniciar tkinter en una variable
aplicacion = Tk()

# Ajustar el tamaño de la ventana y su ubicación
# Tamaño, eje x y eje y
aplicacion.geometry('1250x550+600+200')

# Evitar maximizar pantalla
# eje x y eje y
aplicacion.resizable(0, 0)

# Titulo de la ventana
aplicacion.title('Mi restaurant - Sistema de facturación')

# Color de fondo
aplicacion.config(bg='burlywood')


"""
Configuración de los paneles
"""

# PANEL SUPERIOR
# Configuración de la ubicación, del borde
# y el tipo de relieve
panel_superior = Frame(
    aplicacion,
    bd=1,
    relief=FLAT
)
# Posición dentro de la ubicación
panel_superior.pack(side=TOP)

# Etiqueta título
etiqueta_titulo = Label(
    panel_superior,
    text='Sistema de Facturación',
    fg='gray25',
    font=('Ubuntu', 46),
    bg='burlywood',
    width=27
)

# Posición del título mediante fila y columna
etiqueta_titulo.grid(row=0, column=0)


# PANEL IZQUIERDO
# Configuración de la ubicación, del borde
# y el tipo de relieve
panel_izquierdo = Frame(
    aplicacion,
    bd=11,
    relief=FLAT
)
# Posición dentro de la ubicación
panel_izquierdo.pack(side=LEFT)


# PANEL INFERIOR
# dentro de panel izquierdo - COSTOS
# Configuración de la ubicación, del borde
# y el tipo de relieve
panel_costos = Frame(
    panel_izquierdo,
    bd=10,
    relief=FLAT,
    bg='azure4',
    padx=50
)
# Posición dentro de la ubicación
panel_costos.pack(side=BOTTOM)

# PANEL IZQUIERDO IZQUIERDA
# dentro de panel izquierdo - COMIDAS
# Configuración de la ubicación, del borde
# y el tipo de relieve. Pero con LabelFrame...
panel_comidas = LabelFrame(
    panel_izquierdo,
    text='Comida',
    font=('Ubuntu', 18, 'bold'),
    bd=5,
    relief=FLAT,
    fg='gray25'
)

# Posición dentro de la ubicación
panel_comidas.pack(side=LEFT)


# PANEL IZQUIERDO CENTRO
# dentro de panel izquierdo - BEBIDAS
# Configuración de la ubicación, del borde
# y el tipo de relieve. Pero con LabelFrame...
panel_bebidas = LabelFrame(
    panel_izquierdo,
    text='Bebidas',
    font=('Ubuntu', 18, 'bold'),
    bd=5,
    relief=FLAT,
    fg='gray25'
)

# Posición dentro de la ubicación
# Se coloca después del anterior
panel_bebidas.pack(side=LEFT)


# PANEL IZQUIERDO DERECHA
# dentro de panel izquierdo - POSTRES
# Configuración de la ubicación, del borde
# y el tipo de relieve. Pero con LabelFrame...
panel_postres = LabelFrame(
    panel_izquierdo,
    text='Postres',
    font=('Ubuntu', 18, 'bold'),
    bd=5,
    relief=FLAT,
    fg='gray25'
)
# Posición dentro de la ubicación
# Se coloca después del anterior
panel_postres.pack(side=LEFT)


# PANEL DERECHO
# Configuración de la ubicación, del borde
# y el tipo de relieve
panel_derecha = Frame(
    aplicacion,
    bd=1,
    relief=FLAT
)
# Posición dentro de la ubicación
panel_derecha.pack(side=RIGHT)


# PANEL DERECHO SUPERIOR
# dentro de panel derecho - CALCULADORA
# Configuración de la ubicación, del borde
# y el tipo de relieve.
panel_calculadora = Frame(
    panel_derecha,
    bd=1,
    relief=FLAT,
    bg='burlywood'
)
# Posición dentro de la ubicación
# Por defecto, se coloca arriba
panel_calculadora.pack()


# PANEL DERECHO CENTRO
# dentro de panel derecho - RECIBO
# Configuración de la ubicación, del borde
# y el tipo de relieve.
panel_recibo = Frame(
    panel_derecha,
    bd=1,
    relief=FLAT,
    bg='burlywood'
)
# Posición dentro de la ubicación
# Por defecto, se coloca arriba después del anterior
panel_recibo.pack()


# PANEL DERECHO INFERIOR
# dentro de panel derecho - BOTONES
# Configuración de la ubicación, del borde
# y el tipo de relieve.
panel_botones = Frame(
    panel_derecha,
    bd=1,
    relief=FLAT,
    bg='burlywood'
)
# Posición dentro de la ubicación
# Por defecto, se coloca arriba después del anterior
panel_botones.pack()


"""
Configuración de los contenidos
"""

# Lista de productos

lista_comidas = [
    'pollo',
    'cordero',
    'salmon',
    'merluza',
    'verdura',
    'kebab',
    'pizza1',
    'pizza2',
    'pizza3'
]

lista_bebidas = [
    'agua',
    'soda',
    'jugo',
    'refresco1',
    'refresco2',
    'cerveza1',
    'cerveza2',
    'vino1',
    'vino2'
]

lista_postres = [
    'helado',
    'fruta',
    'brownie',
    'yogur',
    'flan',
    'mouse',
    'pastel1',
    'pastel2',
    'pastel3'
]


"""
Configuración de las listas de contenidos, checkbox y campos de entrada
"""

# GENERAR ITEMS COMIDA
# Variable de lista dinámica para recoger el valor
# true o false (1 o 0) de cada comida
variables_comida = []
# Se necesitara almacenar el número de elementos solicitados
# para eso un cuadro y el texto que contenga
cuadros_comida = []
texto_comida = []

# Variable de contador para el loop
contador = 0
# Creación de Checkbutton mediante loop
for comida in lista_comidas:

    # Creamos el espacio string vacío en la lista
    variables_comida.append('')
    # Entramos en el espacio vacío
    # y le asignamos el valor Intenger Variable de tkinter
    variables_comida[contador] = IntVar()

    # Check de cada elemento
    comida = Checkbutton(
        panel_comidas,
        text=comida.title(),
        font=('Ubuntu', 16, 'bold'),
        fg='gray40',
        onvalue=1,                          # Valor cuando este activada
        offvalue=0,                         # Valor cuando este desactivado
        variable=variables_comida[contador],  # Le damos el valor del check
        command=revisar_check                  # Llamada a la función
    )

    # Ubicación de la lista con checks
    comida.grid(
        row=contador,
        column=0,
        sticky=W
    )

    # Crear cuadros de entrada de texto
    # Creamos el espacio string vacío en las listas
    cuadros_comida.append('')
    texto_comida.append('')
    # Valor por defecto en el cuadro de texto con StringVar de tkinter
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')

    # Añadimos un cuadro de entrada tkinter
    cuadros_comida[contador] = Entry(
        panel_comidas,
        font=('Ubuntu', 16, 'bold'),
        bd=1,
        width=6,
        state=DISABLED,      # A priori lo desactivamos hasta que no este el checkbox
        # Asociamos el cuadro input a la variable
        textvariable=texto_comida[contador]
    )
    # Ubicación de los cuadros de inputs
    cuadros_comida[contador].grid(row=contador, column=1)

    # Sumar al contador
    contador += 1


# GENERAR ITEMS BEBIDA
# Variable de lista dinámica para recoger el valor
# true o false (1 o 0) de cada bebida
variables_bebida = []
# Se necesitara almacenar el número de elementos solicitados
# para eso un cuadro y el texto que contenga
cuadros_bebida = []
texto_bebida = []

# Variable de contador para el loop
contador = 0
# Creación de Checkbutton mediante loop
for bebida in lista_bebidas:

    # Creamos el espacio string vacío en la lista
    variables_bebida.append('')
    # Entramos en el espacio vacío
    # y le asignamos el valor Intenger Variable
    variables_bebida[contador] = IntVar()

    # Check de cada elemento
    bebida = Checkbutton(
        panel_bebidas,
        text=bebida.title(),
        font=('Ubuntu', 16, 'bold'),
        fg='gray40',
        onvalue=1,                          # Valor cuando este activada
        offvalue=0,                         # Valor cuando este desactivado
        variable=variables_bebida[contador],  # Le damos el valor del check
        command=revisar_check                  # Llamada a la función
    )

    # Ubicación de la lista con checks
    bebida.grid(
        row=contador,
        column=0,
        sticky=W
    )

    # Crear cuadros de entrada de texto
    # Creamos el espacio string vacío en las listas
    cuadros_bebida.append('')
    texto_bebida.append('')
    # Valor por defecto en el cuadro de texto con StringVar de tkinter
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')

    # Añadimos un cuadro de entrada tkinter
    cuadros_bebida[contador] = Entry(
        panel_bebidas,
        font=('Ubuntu', 16, 'bold'),
        bd=1,
        width=6,
        state=DISABLED,      # A priori lo desactivamos hasta que no este el checkbox
        # Asociamos el cuadro input a la variable
        textvariable=texto_bebida[contador]
    )
    # Ubicación de los cuadros de inputs
    cuadros_bebida[contador].grid(row=contador, column=1)

    # Sumar al contador
    contador += 1


# GENERAR ITEMS POSTRES
# Variable de lista dinámica para recoger el valor
# true o false (1 o 0) de cada postre
variables_postre = []
# Se necesitara almacenar el número de elementos solicitados
# para eso un cuadro y el texto que contenga
cuadros_postre = []
texto_postre = []

# Variable de contador para el loop
contador = 0
# Creación de Checkbutton mediante loop
for postre in lista_postres:

    # Creamos el espacio string vacío en la lista
    variables_postre.append('')
    # Entramos en el espacio vacío
    # y le asignamos el valor Intenger Variable
    variables_postre[contador] = IntVar()

    # Check de cada elemento
    postre = Checkbutton(
        panel_postres,
        text=postre.title(),
        font=('Ubuntu', 16, 'bold'),
        fg='gray40',
        onvalue=1,                          # Valor cuando este activada
        offvalue=0,                         # Valor cuando este desactivado
        variable=variables_postre[contador],  # Le damos el valor del check
        command=revisar_check                  # Llamada a la función
    )

    # Ubicación de la lista con checks
    postre.grid(
        row=contador,
        column=0,
        sticky=W
    )

    # Crear cuadros de entrada de texto
    # Creamos el espacio string vacío en las listas
    cuadros_postre.append('')
    texto_postre.append('')
    # Valor por defecto en el cuadro de texto con StringVar de tkinter
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')

    # Añadimos un cuadro de entrada tkinter
    cuadros_postre[contador] = Entry(
        panel_postres,
        font=('Ubuntu', 16, 'bold'),
        bd=1,
        width=6,
        state=DISABLED,      # A priori lo desactivamos hasta que no este el checkbox
        # Asociamos el cuadro input a la variable
        textvariable=texto_postre[contador]
    )
    # Ubicación de los cuadros de inputs
    cuadros_postre[contador].grid(row=contador, column=1)

    # Sumar al contador
    contador += 1


"""
Configurar etiquetas de costos y campos de entrada
"""

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# COSTO COMIDA

etiqueta_costo_comida = Label(
    panel_costos,
    text='Costo Comida',
    font=('Ubuntu', 14, 'bold'),
    bg='azure4',
    fg='white'
)

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(
    panel_costos,
    font=('Ubuntu', 14, 'bold'),
    bd=1,
    width=10,
    state='readonly',
    textvariable=var_costo_comida
)

texto_costo_comida.grid(row=0, column=1, padx=16)


# COSTO BEBIDA

etiqueta_costo_bebida = Label(
    panel_costos,
    text='Costo Bebida',
    font=('Ubuntu', 14, 'bold'),
    bg='azure4',
    fg='white'
)

etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(
    panel_costos,
    font=('Ubuntu', 14, 'bold'),
    bd=1,
    width=10,
    state='readonly',
    textvariable=var_costo_bebida
)

texto_costo_bebida.grid(row=1, column=1, padx=16)


# COSTO POSTRE

etiqueta_costo_postre = Label(
    panel_costos,
    text='Costo Postre',
    font=('Ubuntu', 14, 'bold'),
    bg='azure4',
    fg='white'
)

etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(
    panel_costos,
    font=('Ubuntu', 14, 'bold'),
    bd=1,
    width=10,
    state='readonly',
    textvariable=var_costo_postre
)

texto_costo_postre.grid(row=2, column=1, padx=16)


# SUBTOTAL

etiqueta_subtotal = Label(
    panel_costos,
    text='Subtotal',
    font=('Ubuntu', 14, 'bold'),
    bg='azure4',
    fg='white'
)

etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(
    panel_costos,
    font=('Ubuntu', 14, 'bold'),
    bd=1,
    width=10,
    state='readonly',
    textvariable=var_subtotal
)

texto_subtotal.grid(row=0, column=3, padx=16)


# IMPUESTOS

etiqueta_impuesto = Label(
    panel_costos,
    text='Impuesto',
    font=('Ubuntu', 14, 'bold'),
    bg='azure4',
    fg='white'
)

etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(
    panel_costos,
    font=('Ubuntu', 14, 'bold'),
    bd=1,
    width=10,
    state='readonly',
    textvariable=var_impuesto
)

texto_impuesto.grid(row=1, column=3, padx=16)


# TOTAL

etiqueta_total = Label(
    panel_costos,
    text='Total',
    font=('Ubuntu', 14, 'bold'),
    bg='azure4',
    fg='white'
)

etiqueta_total.grid(row=2, column=2)

texto_total = Entry(
    panel_costos,
    font=('Ubuntu', 14, 'bold'),
    bd=2,
    width=10,
    state='readonly',
    textvariable=var_total
)

texto_total.grid(row=2, column=3, padx=16)


"""
Configurar Botones
"""

# Lista de botones
botones = [
    'total',
    'recibo',
    'guardar',
    'resetear'
]

botones_creados = []
# Contador de columnas
columnas = 0


for boton in botones:
    boton = Button(
        panel_botones,
        text=boton.title(),
        font=('Ubuntu', 14, 'bold'),
        fg='white',
        bg='CadetBlue',
        bd=1,
        width=10
    )

    botones_creados.append(boton)

    boton.grid(row=0, column=columnas)

    columnas += 1

# Añadir funcionalidad al botón total
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)


"""
Configurar area de recibo
"""

texto_recibo = Text(
    panel_recibo,
    font=('Ubuntu', 14, 'bold'),
    bd=2,
    width=50,
    height=10
)

texto_recibo.grid(row=0, column=0)


"""
Calculadora
"""
visor_calculadora = Entry(
    panel_calculadora,
    font=('Ubuntu', 14, 'bold'),
    bd=2,
    width=50
)

visor_calculadora.grid(
    row=0,
    column=0,
    columnspan=4
)

# Variables de listas
botones_calculadora = [
    '7',
    '8',
    '9',
    '+',
    '4',
    '5',
    '6',
    '-',
    '1',
    '2',
    '3',
    'x',
    '=',
    'Borrar',
    '0',
    '/'
]

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(
        panel_calculadora,
        text=boton.title(),
        font=('ubuntu', 14, 'bold'),
        fg='white',
        bg='CadetBlue',
        bd=1,
        width=10
    )

    # Guardamos en la lista los botones marcados
    botones_guardados.append(boton)

    # Ubicamos los botones en el panel
    boton.grid(row=fila, column=columna)

    if columna == 3:

        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

# Añadimos el valor de los botones a la función de click
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))


"""
FINAL - Se debe mantener abierta la pantalla hasta el final
"""

# Evitar que la pantalla se cierre
aplicacion.mainloop()
