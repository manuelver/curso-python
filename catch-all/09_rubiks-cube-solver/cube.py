"""
Este es el Solucionador de Cubos
Esta versión contiene una interfaz gráfica
Última edición el: 05/12/2014
Escrito originalmente por: 
- Lucas Liberacki (https://github.com/CubeLuke) 
- & Tom Brannan (https://github.com/TomBrannan)
Modificado por manuelver
"""

from random import randint
from tkinter import *

import copy
import webbrowser
import os
import tkinter as tk


# Variables globales
moves_list = []
last_scramble = []
f2l_list = []
step_moves_list = []
solution_length = 0


# creates a 3d list representing a solved cube
def make_cube():
    global step_moves_list, f2l_list, moves_list
    step_moves_list = [0, 0, 0, 0]
    f2l_list = []
    moves_list = []
    return [[
            ['W', 'W', 'W'],
            ['W', 'W', 'W'],
            ['W', 'W', 'W']],  # Arriba/blanco

            [['G', 'G', 'G'],
            ['G', 'G', 'G'],
            ['G', 'G', 'G']],  # Frontal/verde

            [['R', 'R', 'R'],
            ['R', 'R', 'R'],
            ['R', 'R', 'R']],  # Derecha/rojo

            [['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']],  # Izquierda/naranja

            [['Y', 'Y', 'Y'],
            ['Y', 'Y', 'Y'],
            ['Y', 'Y', 'Y']],  # Abajo/amarillo

            [['B', 'B', 'B'],
            ['B', 'B', 'B'],
            ['B', 'B', 'B']  # Trasero/azul
        ]]


a = make_cube()


# Imprime una representación en cadena del cubo en el intérprete
def print_cube():
    print('\t\t'+str(a[5][0])+'\n\t\t'+str(a[5][1])+'\n\t\t'+str(a[5][2]))
    print(str(a[3][0])+' '+str(a[0][0])+' '+str(a[2][0]))
    print(str(a[3][1])+' '+str(a[0][1])+' '+str(a[2][1]))
    print(str(a[3][2])+' '+str(a[0][2])+' '+str(a[2][2]))
    print('\t\t'+str(a[1][0])+'\n\t\t'+str(a[1][1])+'\n\t\t'+str(a[1][2]))
    print('\t\t'+str(a[4][0])+'\n\t\t'+str(a[4][1])+'\n\t\t'+str(a[4][2]))


# Simplifica la lista de movimientos y devuelve una representación en cadena de 
# los movimientos
def get_moves():
    simplify_moves()
    s = ""
    for i in moves_list:
        s += str(i) + " "
    s = str.replace(s, "i", "'")[:-1]
    return s


# Devuelve una representación en cadena del último scramble
def get_scramble():
    s = ""
    for i in last_scramble:
        s += str(i) + " "
    s = str.replace(s, "i", "'")[:-1]
    return s


# Función auxiliar: 
# devuelve True si todos los elementos en un conjunto son iguales
def all_same(items):
    return all(x == items[0] for x in items)


# Transforma un movimiento dado en el movimiento correspondiente después de una 
# rotación Y
def yTransform(move):
    if move[0] in ["U", "D"]:
        return move
    if move[0] == "F":
        return "R" + move[1:]
    if move[0] == "R":
        return "B" + move[1:]
    if move[0] == "B":
        return "L" + move[1:]
    if move[0] == "L":
        return "F" + move[1:]
    raise Exception("Invalid move to yTransform: " + move)


# Modifica la lista global de movimientos eliminando redundancias
def simplify_moves():
    global moves_list, solution_length
    new_list = []
    prev_move = ""
    yCount = 0
    for move in moves_list:
        if move == "Y":
            yCount += 1
            yCount %= 4
            continue
        if move == "Yi":
            yCount += 3
            yCount %= 4
            continue
        if move == "Y2":
            yCount += 2
            yCount %= 4
            continue
        if yCount > 0:
            for i in range(yCount):
                move = yTransform(move)
        if prev_move == "" or prev_move == '':
            prev_move = move
            new_list.append(move)
            continue
        if move[0] == prev_move[0]:
            if len(move) == 1:
                if len(prev_move) <= 1:
                    del new_list[-1]
                    mv = move[0] + "2"
                    new_list.append(mv)
                    prev_move = mv
                    continue
                if prev_move[1] == "i":
                    del new_list[-1]
                    prev_move = new_list[-1] if len(new_list) > 0 else ""
                    continue
                if prev_move[1] == "2":
                    del new_list[-1]
                    mv = move[0] + "i"
                    new_list.append(mv)
                    prev_move = mv
                    continue
            if move[1] == "i":
                if len(prev_move) == 1:
                    del new_list[-1]
                    prev_move = new_list[-1] if len(new_list) > 0 else ""
                    continue
                if prev_move[1] == "i":
                    del new_list[-1]
                    mv = move[0] + "2"
                    new_list.append(mv)
                    prev_move = mv
                    continue
                if prev_move[1] == "2":
                    del new_list[-1]
                    mv = move[0]
                    new_list.append(mv)
                    prev_move = mv
                    continue
            if move[1] == "2":
                if len(prev_move) == 1:
                    del new_list[-1]
                    mv = move[0] + "i"
                    new_list.append(mv)
                    prev_move = mv
                    continue
                if prev_move[1] == "i":
                    del new_list[-1]
                    mv = move[0]
                    new_list.append(mv)
                    prev_move = mv
                    continue
                if prev_move[1] == "2":
                    del new_list[-1]
                    prev_move = new_list[-1] if len(new_list) > 0 else ""
                    continue
        new_list.append(move)
        prev_move = move
    solution_length = len(new_list)
    moves_list = new_list


# Configura el cubo para realizar un movimiento rotando esa cara hacia arriba
def setup(face):
    face = str.lower(face)
    if face == "f":
        move("X")
    elif face == "r":
        move("Zi")
    elif face == "l":
        move("Z")
    elif face == "d":
        move("X2")
    elif face == "b":
        move("Xi")
    else:
        raise Exception("Invalid setup; face: " + face)


# Realiza la inversa de setup para restaurar la orientación previa del cubo
def undo(face):
    face = str.lower(face)
    if face == "f":
        move("Xi")
    elif face == "r":
        move("Z")
    elif face == "l":
        move("Zi")
    elif face == "d":
        move("X2")
    elif face == "b":
        move("X")
    else:
        raise Exception("Invalid undo; face: " + face)


# Tokeniza una cadena de movimientos
def m(s):
    s = str.replace(s, "'", "i")
    k = s.split(' ')
    global moves_list, solution_length
    solution_length += len(k)
    for word in k:
        moves_list.append(word)
        move(word)


# Realiza un movimiento configurando, ejecutando movimientos U y deshaciendo la 
# configuración
def move(mv):
    mv = str.lower(mv)
    if mv == "u":
        U()
    elif mv == "u2":
        move("U")
        move("U")
    elif mv == "ui":
        move("U")
        move("U")
        move("U")
    elif mv == "f":
        setup("F")
        U()
        undo("F")
    elif mv == "f2":
        move("F")
        move("F")
    elif mv == "fi":
        move("F")
        move("F")
        move("F")
    elif mv == "r":
        setup("R")
        U()
        undo("R")
    elif mv == "r2":
        move("R")
        move("R")
    elif mv == "ri":
        move("R")
        move("R")
        move("R")
    elif mv == "l":
        setup("L")
        U()
        undo("L")
    elif mv == "l2":
        move("L")
        move("L")
    elif mv == "li":
        move("L")
        move("L")
        move("L")
    elif mv == "b":
        setup("B")
        U()
        undo("B")
    elif mv == "b2":
        move("B")
        move("B")
    elif mv == "bi":
        move("B")
        move("B")
        move("B")
    elif mv == "d":
        setup("D")
        U()
        undo("D")
    elif mv == "d2":
        move("D")
        move("D")
    elif mv == "di":
        move("D")
        move("D")
        move("D")
    elif mv == "x":
        rotate("X")
    elif mv == "x2":
        move("X")
        move("X")
    elif mv == "xi":
        move("X")
        move("X")
        move("X")
    elif mv == "y":
        rotate("Y")
    elif mv == "y2":
        move("Y")
        move("Y")
    elif mv == "yi":
        move("Y")
        move("Y")
        move("Y")
    elif mv == "z":
        rotate("Z")
    elif mv == "z2":
        move("Z")
        move("Z")
    elif mv == "zi":
        move("Z")
        move("Z")
        move("Z")
    elif mv == "uw":
        move("D")
        move("Y")
    elif mv == "uw2":
        move("UW")
        move("UW")
    elif mv == "uwi":
        move("UW")
        move("UW")
        move("UW")
    elif mv == "m":
        move("Li")
        move("R")
        move("Xi")
    elif mv == "mi":
        move("M")
        move("M")
        move("M")
    elif mv == "m2":
        move("M")
        move("M")
    elif mv == "rw":
        move("L")
        move("X")
    elif mv == "rwi":
        move("RW")
        move("RW")
        move("RW")
    elif mv == "rw2":
        move("RW")
        move("RW")
    elif mv == "fw":
        move("Bi")
        move("Z")
    elif mv == "fwi":
        move("FW")
        move("FW")
        move("FW")
    elif mv == "fw2":
        move("FW")
        move("FW")
    elif mv == "lw":
        move("R")
        move("Xi")
    elif mv == "lwi":
        move("LW")
        move("LW")
        move("LW")
    elif mv == "lw2":
        move("LW")
        move("LW")
    elif mv == "bw":
        move("F")
        move("Zi")
    elif mv == "bwi":
        move("BW")
        move("BW")
        move("BW")
    elif mv == "bw2":
        move("BW")
        move("BW")
    elif mv == "dw":
        move("U")
        move("Yi")
    elif mv == "dwi":
        move("DW")
        move("DW")
        move("DW")
    elif mv == "dw2":
        move("DW")
        move("DW")
    else:
        raise Exception("Invalid Move: " + str(mv))



# rota todo el cubo a lo largo de un eje particular
def rotate(axis):
    axis = str.lower(axis)
    if axis == 'x':  # R
        temp = a[0]
        a[0] = a[1]
        a[1] = a[4]
        a[4] = a[5]
        a[5] = temp
        rotate_face_counterclockwise("L")
        rotate_face_clockwise("R")
    elif axis == 'y':  # U
        temp = a[1]
        a[1] = a[2]
        a[2] = a[5]
        a[5] = a[3]
        a[3] = temp
        # después de los intercambios,
        rotate_face_clockwise("L")
        rotate_face_clockwise("F")
        rotate_face_clockwise("R")
        rotate_face_clockwise("B")
        rotate_face_clockwise("U")
        rotate_face_counterclockwise("D")
    elif axis == 'z':  # F
        temp = a[0]
        a[0] = a[3]
        a[3] = a[4]
        a[4] = a[2]
        a[2] = temp
        rotate_face_clockwise("L")
        rotate_face_clockwise("L")
        rotate_face_clockwise("D")
        rotate_face_clockwise("D")
        rotate_face_clockwise("F")
        rotate_face_counterclockwise("B")
    else:
        raise Exception("Rotation inválida: " + axis)


# realiza un movimiento U
def U():
    # rota la cara U
    temp = a[0][0][0]
    a[0][0][0] = a[0][2][0]
    a[0][2][0] = a[0][2][2]
    a[0][2][2] = a[0][0][2]
    a[0][0][2] = temp
    temp = a[0][0][1]
    a[0][0][1] = a[0][1][0]
    a[0][1][0] = a[0][2][1]
    a[0][2][1] = a[0][1][2]
    a[0][1][2] = temp

    # rota otros
    temp = a[5][2][0]
    a[5][2][0] = a[3][2][2]
    a[3][2][2] = a[1][0][2]
    a[1][0][2] = a[2][0][0]
    a[2][0][0] = temp
    temp = a[5][2][1]
    a[5][2][1] = a[3][1][2]
    a[3][1][2] = a[1][0][1]
    a[1][0][1] = a[2][1][0]
    a[2][1][0] = temp
    temp = a[5][2][2]
    a[5][2][2] = a[3][0][2]
    a[3][0][2] = a[1][0][0]
    a[1][0][0] = a[2][2][0]
    a[2][2][0] = temp


# Rota una cara particular en sentido antihorario
def rotate_face_counterclockwise(face):
    rotate_face_clockwise(face)
    rotate_face_clockwise(face)
    rotate_face_clockwise(face)


# Rota una cara particular en sentido horario
def rotate_face_clockwise(face):
    f_id = -1
    face = str.lower(face)
    if face == "u":
        f_id = 0
    elif face == "f":
        f_id = 1
    elif face == "r":
        f_id = 2
    elif face == "l":
        f_id = 3
    elif face == "d":
        f_id = 4
    elif face == "b":
        f_id = 5
    else:
        raise Exception("Cara inválida: " + face)
    temp = a[f_id][0][0]
    a[f_id][0][0] = a[f_id][2][0]
    a[f_id][2][0] = a[f_id][2][2]
    a[f_id][2][2] = a[f_id][0][2]
    a[f_id][0][2] = temp
    temp = a[f_id][0][1]
    a[f_id][0][1] = a[f_id][1][0]
    a[f_id][1][0] = a[f_id][2][1]
    a[f_id][2][1] = a[f_id][1][2]
    a[f_id][1][2] = temp


# Mezcla aleatoriamente el cubo dado un número de movimientos, o dada una lista 
# de movimientos
def scramble(moves=25):
    global last_scramble, moves_list, solution_length, a
    a = make_cube()
    if hasattr(moves, '__iter__'):  # mezcla dada una lista de movimientos
        m(moves)
        moves_list = []
        solution_length = 0
        temp = moves.split(' ')
        last_scramble = temp
    else:  # mezcla aleatoriamente un cierto número de veces
        moves_list = []  # reiniciar moves_list
        last_scramble = []  # reiniciar última mezcla
        prevMove = ""
        for i in range(moves):
            while True:
                thisMove = ""
                r = randint(0, 5)
                if r == 0:
                    thisMove += "U"
                elif r == 1:
                    thisMove += "F"
                elif r == 2:
                    thisMove += "R"
                elif r == 3:
                    thisMove += "L"
                elif r == 4:
                    thisMove += "D"
                elif r == 5:
                    thisMove += "B"
                if thisMove == "U" and prevMove != "U" and prevMove != "D":
                    break
                if thisMove == "F" and prevMove != "F" and prevMove != "B":
                    break
                if thisMove == "R" and prevMove != "R" and prevMove != "L":
                    break
                if thisMove == "L" and prevMove != "L" and prevMove != "R":
                    break
                if thisMove == "D" and prevMove != "D" and prevMove != "U":
                    break
                if thisMove == "B" and prevMove != "B" and prevMove != "F":
                    break
            r = randint(0, 3)
            if r == 1:
                move(thisMove + "i")
                last_scramble.append(thisMove + "i")
            elif r == 2:
                move(thisMove + "2")
                last_scramble.append(thisMove + "2")
            else:
                move(thisMove)
                last_scramble.append(thisMove)
            prevMove = thisMove


# Resuelve el cruce superior como parte del paso OLL
def topCross():
    # si todos los bordes son iguales entre sí (todos siendo blancos)
    if a[0][0][1] == a[0][1][0] == a[0][1][2] == a[0][2][1]:
        # print("Cruce ya hecho, paso omitido")
        return
        # Si esto es cierto, tenemos nuestro cruce y podemos pasar al siguiente 
        # paso
    else:
        while a[0][0][1] != "W" or a[0][1][0] != "W" or a[0][1][2] != "W" or a[0][2][1] != "W":
            if a[0][1][0] == a[0][1][2]:
                # si tenemos una línea horizontal, solo haz el algoritmo
                m("F R U Ri Ui Fi")
                break  # rompiendo sin tener que revisar las condiciones 
                       # mientras de nuevo, esto nos dará un cruce
            elif a[0][0][1] == a[0][2][1]:
                # si tenemos una línea vertical, haz un U y luego el algoritmo
                m("U F R U Ri Ui Fi")
                break
            elif a[0][0][1] != "W" and a[0][1][0] != "W" and a[0][1][2] != "W" and a[0][2][1] != "W":
                # Esto significaría que tenemos un caso de punto, así que 
                # realiza el algoritmo
                m("F U R Ui Ri Fi U F R U Ri Ui Fi")
                break
            elif a[0][1][2] == a[0][2][1] or a[0][0][1] == a[0][1][0]:
                # Si tenemos un caso de L en la parte superior izquierda o la 
                # inferior derecha, nos dará una línea
                m("F R U Ri Ui Fi")
            else:
                # Esto es si no tenemos una línea, punto, cruce, o L en la parte
                # superior izquierda o inferior derecha
                m("U")


# devuelve True si la parte superior está resuelta
def isTopSolved():
    # determina si la parte superior del cubo está resuelta.
    if a[0][0][0] == a[0][0][1] == a[0][0][2] == a[0][1][0] == a[0][1][1] == a[0][1][2] == a[0][2][0] == a[0][2][1] == a[0][2][2]:
        return True
    else:
        return False


# Coloca una sola pieza de borde en la ubicación correcta para el cruce
# Asume que el cruce está formado en la parte inferior y es la cara amarilla
# Verifica todos los bordes en la cara frontal/superior, luego en la parte trasera-derecha/izquierda si es necesario
def putCrossEdge():
    global moves_list
    for i in range(3):
        if i == 1:
            m("Ri U R F2")  # bring out back-right edge
        elif i == 2:
            m("L Ui Li F2")  # bring out back-left edge
        for j in range(4):
            for k in range(4):
                if "Y" in [a[4][0][1], a[1][2][1]]:
                    return
                m("F")
            m("U")


# Realiza el primer paso de la solución: el cruce
def cross():
    for i in range(4):
        putCrossEdge()
        assert "Y" in [a[4][0][1], a[1][2][1]]
        if a[1][2][1] == "Y":
            m("Fi R U Ri F2")  # orient if necessary
        m("Di")

    # permutar para corregir la cara: mueve la cara hacia abajo hasta que 2 
    # estén alineadas, luego intercambia los otros 2 si necesitan ser 
    # intercambiados
    condition = False
    while not condition:
        fSame = a[1][1][1] == a[1][2][1]
        rSame = a[2][1][1] == a[2][1][2]
        bSame = a[5][1][1] == a[5][0][1]
        lSame = a[3][1][1] == a[3][1][0]
        condition = (fSame, rSame, bSame, lSame).count(True) >= 2
        if not condition:
            m("D")
    if (fSame, rSame, bSame, lSame).count(True) == 4:
        return
    assert (fSame, rSame, bSame, lSame).count(True) == 2
    if not fSame and not bSame:
        m("F2 U2 B2 U2 F2")  # intercambiar frente-atras
    elif not rSame and not lSame:
        m("R2 U2 L2 U2 R2")  # intercambiar derecha-izquierda
    elif not fSame and not rSame:
        m("F2 Ui R2 U F2")  # intercambiar frente-derecha
    elif not rSame and not bSame:
        m("R2 Ui B2 U R2")  # intercambiar derecha-atras
    elif not bSame and not lSame:
        m("B2 Ui L2 U B2")  # intercambiar atras-izquierda
    elif not lSame and not fSame:
        m("L2 Ui F2 U L2")  # intercambiar izquierda-frente
    fSame = a[1][1][1] == a[1][2][1]
    rSame = a[2][1][1] == a[2][1][2]
    bSame = a[5][1][1] == a[5][0][1]
    lSame = a[3][1][1] == a[3][1][0]
    assert all([fSame, rSame, bSame, lSame])


# Esto usa todos los algoritmos de f2l para resolver todos los casos posibles
def solveFrontSlot():
    # Esto será F2L, con los 42 casos
    rmid = a[2][1][1]
    fmid = a[1][1][1]
    dmid = a[4][1][1]
    # Orientaciones de las esquinas si están en la capa U, la primera letra 
    # indica la dirección en la que el color está mirando
    fCorU = a[1][0][2] == dmid and a[0][2][2] == fmid and a[2][2][0] == rmid
    rCorU = a[2][2][0] == dmid and a[1][0][2] == fmid and a[0][2][2] == rmid
    uCorU = a[0][2][2] == dmid and a[2][2][0] == fmid and a[1][0][2] == rmid
    # Orientaciones de las esquinas para la ubicación correcta en la capa D
    fCorD = a[1][2][2] == dmid and a[2][2][2] == fmid and a[4][0][2] == rmid
    rCorD = a[2][2][2] == dmid and a[4][0][2] == fmid and a[1][2][2] == rmid
    # Este es el lugar resuelto
    dCorD = a[4][0][2] == dmid and a[1][2][2] == fmid and a[2][2][2] == rmid
    # Orientaciones de los bordes en la capa U, versión normal o invertida 
    # basada en la cara F
    norEdgeFU = a[1][0][1] == fmid and a[0][2][1] == rmid
    norEdgeLU = a[3][1][2] == fmid and a[0][1][0] == rmid
    norEdgeBU = a[5][2][1] == fmid and a[0][0][1] == rmid
    norEdgeRU = a[2][1][0] == fmid and a[0][1][2] == rmid
    norEdgeAny = norEdgeFU or norEdgeLU or norEdgeBU or norEdgeRU
    flipEdgeFU = a[0][2][1] == fmid and a[1][0][1] == rmid
    flipEdgeLU = a[0][1][0] == fmid and a[3][1][2] == rmid
    flipEdgeBU = a[0][0][1] == fmid and a[5][2][1] == rmid
    flipEdgeRU = a[0][1][2] == fmid and a[2][1][0] == rmid
    flipEdgeAny = flipEdgeFU or flipEdgeLU or flipEdgeBU or flipEdgeRU
    # orientaciones de los bordes para la inserción normal o invertida en el 
    # lugar.
    # Este es el lugar resuelto
    norEdgeInsert = a[1][1][2] == fmid and a[2][2][1] == rmid
    flipEdgeInsert = a[2][2][1] == fmid and a[1][1][2] == rmid
    # estos son para si los espacios de la parte trasera derecha o delantera 
    # izquierda están abiertos o no
    backRight = a[4][2][2] == dmid and a[5][1][2] == a[5][0][2] == a[5][1][1] and a[2][0][1] == a[2][0][2] == rmid
    frontLeft = a[4][0][0] == dmid and a[1][1][0] == a[1][2][0] == fmid and a[3][2][0] == a[3][2][1] == a[3][1][1]


    if dCorD and norEdgeInsert:
        return
    # Casos fáciles
    elif fCorU and flipEdgeRU:  # Caso 1
        m("U R Ui Ri")
    elif rCorU and norEdgeFU:  # Caso 2
        m("F Ri Fi R")
    elif fCorU and norEdgeLU:  # Caso 3
        m("Fi Ui F")
    elif rCorU and flipEdgeBU:  # Caso 4
        m("R U Ri")
    # Reposicionar el borde
    elif fCorU and flipEdgeBU:  # Caso 5
        m("F2 Li Ui L U F2")
    elif rCorU and norEdgeLU:  # Caso 6
        m("R2 B U Bi Ui R2")
    elif fCorU and flipEdgeLU:  # Caso 7
        m("Ui R U2 Ri U2 R Ui Ri")
    elif rCorU and norEdgeBU:  # Caso 8
        m("U Fi U2 F Ui F Ri Fi R")
    # Reposicionar el borde y voltear la esquina
    elif fCorU and norEdgeBU:  # Caso 9
        m("Ui R Ui Ri U Fi Ui F")
    elif rCorU and flipEdgeLU:  # Caso 10
        if not backRight:
            m("Ri U R2 U Ri")
        else:
            m("Ui R U Ri U R U Ri")
    elif fCorU and norEdgeRU:  # Caso 11
        m("Ui R U2 Ri U Fi Ui F")
    elif rCorU and flipEdgeFU:  # Caso 12
        if not backRight:
            m("Ri U2 R2 U Ri")
        else:
            m("Ri U2 R2 U R2 U R")
    elif fCorU and norEdgeFU:  # Caso 13
        if not backRight:
            m("Ri U R Fi Ui F")
        else:
            m("U Fi U F Ui Fi Ui F")
    elif rCorU and flipEdgeRU:  # Caso 14
        m("Ui R Ui Ri U R U Ri")
    # Separar el par yendo sobre
    elif fCorU and flipEdgeFU:  # Caso 15
        if not backRight:
            m("Ui Ri U R Ui R U Ri")
        elif not frontLeft:
            m("U R Ui Ri D R Ui Ri Di")
        else:
            m("U Ri F R Fi U R U Ri")
    elif rCorU and norEdgeRU:  # Caso 16
        m("R Ui Ri U2 Fi Ui F")
    elif uCorU and flipEdgeRU:  # Caso 17
        m("R U2 Ri Ui R U Ri")
    elif uCorU and norEdgeFU:  # Caso 18
        m("Fi U2 F U Fi Ui F")
    # Par hecho en el lado
    elif uCorU and flipEdgeBU:  # Caso 19
        m("U R U2 R2 F R Fi")
    elif uCorU and norEdgeLU:  # Caso 20
        m("Ui Fi U2 F2 Ri Fi R")
    elif uCorU and flipEdgeLU:  # Caso 21
        m("R B U2 Bi Ri")
    elif uCorU and norEdgeBU:  # Caso 22
        m("Fi Li U2 L F")
    # Casos raros
    elif uCorU and flipEdgeFU:  # Caso 23
        m("U2 R2 U2 Ri Ui R Ui R2")
    elif uCorU and norEdgeRU:  # Caso 24
        m("U Fi Li U L F R U Ri")
    # Esquina en su lugar, borde en la cara U (Todos estos casos también tienen movimientos de preparación en caso de que el borde esté en la orientación incorrecta)
    elif dCorD and flipEdgeAny:  # Caso 25
        if flipEdgeBU:
            m("U")  # movimiento de preparación
        elif flipEdgeLU:
            m("U2")  # movimiento de preparación
        elif flipEdgeFU:
            m("Ui")  # movimiento de preparación
        if not backRight:
            m("R2 Ui Ri U R2")
        else:
            m("Ri Fi R U R Ui Ri F")
    elif dCorD and norEdgeAny:  # Caso 26
        if norEdgeRU:
            m("U")  # movimiento de preparación
        elif norEdgeBU:
            m("U2")  # movimiento de preparación
        elif norEdgeLU:
            m("Ui")  # movimiento de preparación
        m("U R Ui Ri F Ri Fi R")
    elif fCorD and flipEdgeAny:  # Caso 27
        if flipEdgeBU:
            m("U")  # movimiento de preparación
        elif flipEdgeLU:
            m("U2")  # movimiento de preparación
        elif flipEdgeFU:
            m("Ui")  # movimiento de preparación
        m("R Ui Ri U R Ui Ri")
    elif rCorD and norEdgeAny:  # Caso 28
        if norEdgeRU:
            m("U")  # movimiento de preparación
        elif norEdgeBU:
            m("U2")  # movimiento de preparación
        elif norEdgeLU:
            m("Ui")  # movimiento de preparación
        m("R U Ri Ui F Ri Fi R")
    elif fCorD and norEdgeAny:  # Caso 29
        if norEdgeRU:
            m("U")  # movimiento de preparación
        elif norEdgeBU:
            m("U2")  # movimiento de preparación
        elif norEdgeLU:
            m("Ui")  # movimiento de preparación
        m("U2 R Ui Ri Fi Ui F")
    elif rCorD and flipEdgeAny:  # Caso 30
        if flipEdgeBU:
            m("U")  # movimiento de preparación
        elif flipEdgeLU:
            m("U2")  # movimiento de preparación
        elif flipEdgeFU:
            m("Ui")  # movimiento de preparación
        m("R U Ri Ui R U Ri")
    # Borde en su lugar, esquina en la cara U
    elif uCorU and flipEdgeInsert:  # Caso 31
        m("R U2 Ri Ui F Ri Fi R")
    elif uCorU and norEdgeInsert:  # Caso 32
        m("R2 U R2 U R2 U2 R2")
    elif fCorU and norEdgeInsert:  # Caso 33
        m("Ui R Ui Ri U2 R Ui Ri")
    elif rCorU and norEdgeInsert:  # Caso 34
        m("Ui R U2 Ri U R U Ri")
    elif fCorU and flipEdgeInsert:  # Caso 35
        m("U2 R Ui Ri Ui Fi Ui F")
    elif rCorU and flipEdgeInsert:  # Caso 36
        m("U Fi Ui F Ui R U Ri")
    # Borde y esquina en su lugar
    # Caso 37 es el caso Lol, ya completado
    elif dCorD and flipEdgeInsert:  # Caso 38 (Caso típico de par f2l invertido)
        m("R2 U2 F R2 Fi U2 Ri U Ri")
    elif fCorD and norEdgeInsert:  # Caso 39
        m("R2 U2 Ri Ui R Ui Ri U2 Ri")
    elif rCorD and norEdgeInsert:  # Caso 40
        m("R U2 R U Ri U R U2 R2")
    elif fCorD and flipEdgeInsert:  # Caso 41
        m("F2 Li Ui L U F Ui F")
    elif rCorD and flipEdgeInsert:  # Caso 42
        m("R Ui Ri Fi Li U2 L F")


# Devuelve verdadero si la esquina f2l en el lugar FR está insertada y orientada correctamente
def f2lCorner():
    # Este es el lugar resuelto
    return a[4][0][2] == a[4][1][1] and a[1][2][2] == a[1][1][1] and a[2][2][2] == a[2][1][1]


# Devuelve verdadero si el borde f2l en el lugar FR está insertado y orientado correctamente
def f2lEdge():
    # Este es el lugar resuelto
    return a[1][1][2] == a[1][1][1] and a[2][2][1] == a[2][1][1]


# Devuelve verdadero si el borde f2l y la esquina están correctamente insertados y orientados en la posición FR
def f2lCorrect():
    return f2lCorner() and f2lEdge()


# Devuelve verdadero si el borde f2l está en la capa superior en absoluto
def f2lEdgeOnTop():
    rmid = a[2][1][1]
    fmid = a[1][1][1]
    dmid = a[4][1][1]
    # orientaciones del borde en la capa U, versión normal o invertida basada en la cara F
    norEdgeFU = a[1][0][1] == fmid and a[0][2][1] == rmid
    norEdgeLU = a[3][1][2] == fmid and a[0][1][0] == rmid
    norEdgeBU = a[5][2][1] == fmid and a[0][0][1] == rmid
    norEdgeRU = a[2][1][0] == fmid and a[0][1][2] == rmid
    norEdgeAny = norEdgeFU or norEdgeLU or norEdgeBU or norEdgeRU
    flipEdgeFU = a[0][2][1] == fmid and a[1][0][1] == rmid
    flipEdgeLU = a[0][1][0] == fmid and a[3][1][2] == rmid
    flipEdgeBU = a[0][0][1] == fmid and a[5][2][1] == rmid
    flipEdgeRU = a[0][1][2] == fmid and a[2][1][0] == rmid
    flipEdgeAny = flipEdgeFU or flipEdgeLU or flipEdgeBU or flipEdgeRU
    return norEdgeAny or flipEdgeAny


# Devuelve verdadero si el borde f2l está insertado. Puede estar correctamente orientado o invertido.
def f2lEdgeInserted():
    rmid = a[2][1][1]
    fmid = a[1][1][1]
    # orientaciones del borde para la inserción normal o invertida en el lugar
    # Este es el lugar resuelto
    norEdgeInsert = a[1][1][2] == fmid and a[2][2][1] == rmid
    flipEdgeInsert = a[2][2][1] == fmid and a[1][1][2] == rmid
    return norEdgeInsert or flipEdgeInsert


# Esto se usa para determinar si el borde f2l frontal está insertado o no, el parámetro es para el borde solicitado. toma BR, BL y FL como válidos
def f2lEdgeInserted2(p):
    rmid = a[2][1][1]
    fmid = a[1][1][1]
    # orientaciones del borde para la inserción normal o invertida en el lugar
    # Este es el lugar resuelto
    norEdgeInsert = a[1][1][2] == fmid and a[2][2][1] == rmid
    flipEdgeInsert = a[2][2][1] == fmid and a[1][1][2] == rmid
    # Orientaciones del borde en comparación con los colores del Frente y el Derecho
    BR = (a[5][1][2] == fmid and a[2][0][1] == rmid) or (
        a[5][1][2] == rmid and a[2][0][1] == fmid)
    BL = (a[3][0][1] == fmid and a[5][1][0] == rmid) or (
        a[3][0][1] == rmid and a[5][1][0] == fmid)
    FL = (a[3][2][1] == fmid and a[1][1][0] == rmid) or (
        a[3][2][1] == rmid and a[1][1][0] == fmid)

    if p == "BR":
        if BR:
            return True
        else:
            return False
    elif p == "BL":
        if BL:
            return True
        return False
    elif p == "FL":
        if FL:
            return True
        return False
    elif p == "FR":
        if norEdgeInsert or flipEdgeInsert:
            return True
    return False


# Devuelve verdadero si la esquina f2l está insertada, no tiene que estar orientada correctamente
def f2lCornerInserted():
    rmid = a[2][1][1]
    fmid = a[1][1][1]
    dmid = a[4][1][1]
    # Orientaciones de la esquina para la ubicación correcta en la capa D
    fCorD = a[1][2][2] == dmid and a[2][2][2] == fmid and a[4][0][2] == rmid
    rCorD = a[2][2][2] == dmid and a[4][0][2] == fmid and a[1][2][2] == rmid
    # Este es el lugar resuelto
    dCorD = a[4][0][2] == dmid and a[1][2][2] == fmid and a[2][2][2] == rmid
    return fCorD or rCorD or dCorD


# Devuelve verdadero si hay una esquina f2l ubicada en la orientación FR
def f2lFRCor():
    rmid = a[2][1][1]
    fmid = a[1][1][1]
    dmid = a[4][1][1]
    # orientaciones de las esquinas si están en la capa U, la primera letra indica la dirección en la que el color está mirando
    fCorU = a[1][0][2] == dmid and a[0][2][2] == fmid and a[2][2][0] == rmid
    rCorU = a[2][2][0] == dmid and a[1][0][2] == fmid and a[0][2][2] == rmid
    uCorU = a[0][2][2] == dmid and a[2][2][0] == fmid and a[1][0][2] == rmid
    return fCorU or rCorU or uCorU


# Devuelve verdadero si hay un borde f2l ubicado en la posición FU
def f2lFUEdge():
    rmid = a[2][1][1]
    fmid = a[1][1][1]
    norEdgeFU = a[1][0][1] == fmid and a[0][2][1] == rmid
    flipEdgeFU = a[0][2][1] == fmid and a[1][0][1] == rmid
    return norEdgeFU or flipEdgeFU


# Devuelve verdadero si la esquina f2l está ubicada en la capa U
def f2lCornerOnTop():
    wasFound = False
    for i in range(4):  # Realiza 4 movimientos U para encontrar la esquina
        if f2lFRCor():
            wasFound = True
        m("U")
    return wasFound


# Devolverá la ubicación de la esquina que pertenece al lugar FR. Devuelve BR, BL, FL o FR.
def f2lCornerCheck():
    r = "FR"
    count = 0
    while count < 4:
        if count == 0:
            if f2lCornerInserted():
                r = "FR"
        elif count == 1:
            if f2lCornerInserted():
                r = "FL"
        elif count == 2:
            if f2lCornerInserted():
                r = "BL"
        elif count == 3:
            if f2lCornerInserted():
                r = "BR"
        m("D")
        count += 1
    return r


# Devolverá la ubicación del borde que pertenece al lugar FR.
# Devuelve BR, BL, FL o FR.
def f2lEdgeCheck():
    if f2lEdgeInserted2("FL"):
        return "FL"
    elif f2lEdgeInserted2("BL"):
        return "BL"
    elif f2lEdgeInserted2("BR"):
        return "BR"
    elif f2lEdgeInserted2("FR"):
        return "FR"
    else:
        raise Exception("Excepción en f2lEdgeCheck()")


# Esto es para el caso en que el Borde está insertado, pero la esquina no
def f2lEdgeNoCorner():
    topEdgeTop = a[0][2][1]
    topEdgeFront = a[1][0][1]
    rmid = a[2][1][1]
    bmid = a[5][1][1]
    lmid = a[3][1][1]
    fmid = a[1][1][1]
    # Esto es para comparar el borde frontal con otros bordes diversos para algs avanzados/lookahead
    BREdge = (topEdgeTop == rmid or topEdgeTop == bmid) and (
        topEdgeFront == rmid or topEdgeFront == bmid)
    BLEdge = (topEdgeTop == lmid or topEdgeTop == bmid) and (
        topEdgeFront == lmid or topEdgeFront == bmid)
    FLEdge = (topEdgeTop == fmid or topEdgeTop == lmid) and (
        topEdgeFront == fmid or topEdgeFront == lmid)
    if f2lCornerOnTop():
        while True:
            solveFrontSlot()
            if f2lCorrect():
                break
            m("U")
    else:
        if f2lCornerCheck() == "BR":
            if BREdge:
                m("Ri Ui R U2")
            else:
                m("Ri U R U")
        elif f2lCornerCheck() == "BL":
            if BLEdge:
                m("L U Li U")
            else:
                m("L Ui Li U2")
        elif f2lCornerCheck() == "FL":
            if FLEdge:
                m("Li U L Ui")
            else:
                m("Li Ui L")
    solveFrontSlot()

    if not f2lCorrect():
        raise Exception("Excepción encontrada en f2lEdgeNoCorner()")


# Este es el caso para si la esquina está insertada, pero el borde no
def f2lCornerNoEdge():
    topEdgeTop = a[0][2][1]
    topEdgeFront = a[1][0][1]
    rmid = a[2][1][1]
    bmid = a[5][1][1]
    lmid = a[3][1][1]
    fmid = a[1][1][1]
    # Esto es para comparar el borde frontal con otros bordes diversos para algoritmos avanzados/lookahead
    BREdge = (topEdgeTop == rmid or topEdgeTop == bmid) and (
        topEdgeFront == rmid or topEdgeFront == bmid)
    BLEdge = (topEdgeTop == lmid or topEdgeTop == bmid) and (
        topEdgeFront == lmid or topEdgeFront == bmid)
    FLEdge = (topEdgeTop == fmid or topEdgeTop == lmid) and (
        topEdgeFront == fmid or topEdgeFront == lmid)
    if f2lEdgeOnTop():
        while True:
            solveFrontSlot()
            if f2lCorrect():
                break
            m("U")
    else:
        if f2lEdgeCheck() == "BR":
            if BREdge:
                m("Ri Ui R U2")
            else:
                m("Ri U R U")
        elif f2lEdgeCheck() == "BL":
            if BLEdge:
                m("L U Li U")
            else:
                m("L Ui Li U2")
        elif f2lEdgeCheck() == "FL":
            if FLEdge:
                m("Li U L Ui")
            else:
                m("Li Ui L")
    solveFrontSlot()

    if not f2lCorrect():
        raise Exception("Excepción encontrada en f2lCornerNoEdge()")


# Este es el caso para si la esquina está en la parte superior, y el borde no. Ninguno está insertado correctamente. El borde debe estar en otro lugar.
def f2lCornerTopNoEdge():
    topEdgeTop = a[0][2][1]
    topEdgeFront = a[1][0][1]
    rmid = a[2][1][1]
    bmid = a[5][1][1]
    lmid = a[3][1][1]
    fmid = a[1][1][1]
    # Esto es para comparar el borde frontal con otros bordes diversos para algoritmos avanzados/lookahead
    BREdge = (topEdgeTop == rmid or topEdgeTop == bmid) and (
        topEdgeFront == rmid or topEdgeFront == bmid)
    BLEdge = (topEdgeTop == lmid or topEdgeTop == bmid) and (
        topEdgeFront == lmid or topEdgeFront == bmid)
    FLEdge = (topEdgeTop == fmid or topEdgeTop == lmid) and (
        topEdgeFront == fmid or topEdgeFront == lmid)

    # Gira la parte superior hasta que la esquina en la cara U esté en la posición correcta
    while True:
        if f2lFRCor():
            break
        m("U")
    # Verificaremos bordes adicionales para elegir un algoritmo más adecuado para buscar
    if f2lEdgeCheck() == "BR":
        if BREdge:
            m("Ri Ui R")
        else:
            m("Ri U R")
    elif f2lEdgeCheck() == "BL":
        if BLEdge:
            m("U2 L Ui Li")
        else:
            m("L Ui Li U")
    elif f2lEdgeCheck() == "FL":
        if FLEdge:
            m("U2 Li Ui L U2")
        else:
            m("Li Ui L U")
    solveFrontSlot()

    if not f2lCorrect():
        raise Exception("Excepción encontrada en f2lCornerTopNoEdge()")


# Este es el caso para si el borde está en la parte superior, y la esquina no. Ninguno está insertado correctamente. La esquina debe estar en otro lugar.
# La búsqueda para este paso es comparar el borde trasero con los lugares, en lugar del frontal como en otros casos
def f2lEdgeTopNoCorner():
    BackEdgeTop = a[0][0][1]
    BackEdgeBack = a[5][2][1]
    rmid = a[2][1][1]
    bmid = a[5][1][1]
    lmid = a[3][1][1]
    fmid = a[1][1][1]
    rs1 = BackEdgeTop == rmid or BackEdgeTop == bmid
    rs2 = BackEdgeBack == rmid or BackEdgeBack == bmid
    # Esto es para comparar el borde trasero con otros bordes diversos para algoritmos avanzados/lookahead
    BREdge = rs1 and rs2
    BLEdge = (BackEdgeTop == lmid or BackEdgeTop == bmid) and (
        BackEdgeBack == lmid or BackEdgeBack == bmid)
    FLEdge = (BackEdgeTop == fmid or BackEdgeTop == lmid) and (
        BackEdgeBack == fmid or BackEdgeBack == lmid)

    # Gira la parte superior hasta que el borde en la cara U esté en la posición correcta
    while True:
        if f2lFUEdge():
            break
        m("U")
    # Verificaremos bordes adicionales para elegir un algoritmo más adecuado para buscar
    if f2lCornerCheck() == "BR":
        if BREdge:
            m("Ri U R U")
        else:
            m("Ui Ri U R U")
    elif f2lCornerCheck() == "BL":
        if BLEdge:
            m("L Ui Li U2")
        else:
            m("U2 L U2 Li")
    elif f2lCornerCheck() == "FL":
        if FLEdge:
            m("Li Ui L")
        else:
            m("U Li Ui L")
    solveFrontSlot()

    if not f2lCorrect():
        raise Exception("Excepción encontrada en f2lEdgeTopNoCorner()")


# Este es el caso para si el borde o la esquina no están en la parte superior, y no están insertados correctamente. Ambos deben estar en otros lugares.
def f2lNoEdgeOrCorner():
    # La estrategia aquí es primero encontrar la esquina y sacarla. La colocaré en la posición FR donde corresponde
    # Luego verificaré si tengo un caso, y si todo está resuelto.
    # Si no lo tengo resuelto en este punto, tendré que seguir lo que ocurre en f2lCornerTopNoEdge()
    BackEdgeTop = a[0][0][1]
    BackEdgeBack = a[5][2][1]
    rmid = a[2][1][1]
    bmid = a[5][1][1]
    lmid = a[3][1][1]
    fmid = a[1][1][1]
    # Esto es para comparar el borde trasero con otros bordes diversos para algoritmos avanzados/lookahead
    BREdge = (BackEdgeTop == rmid or BackEdgeTop == bmid) and (
        BackEdgeBack == rmid or BackEdgeBack == bmid)
    BLEdge = (BackEdgeTop == lmid or BackEdgeTop == bmid) and (
        BackEdgeBack == lmid or BackEdgeBack == bmid)
    FLEdge = (BackEdgeTop == fmid or BackEdgeTop == lmid) and (
        BackEdgeBack == fmid or BackEdgeBack == lmid)

    # Verificaremos bordes adicionales para elegir un algoritmo más adecuado para buscar
    if f2lCornerCheck() == "BR":
        if BREdge:
            m("Ri U R U")
        else:
            m("Ui Ri U R U")
    elif f2lCornerCheck() == "BL":
        if BLEdge:
            m("L Ui Li U2")
        else:
            m("U2 L U2 Li")
    elif f2lCornerCheck() == "FL":
        if FLEdge:
            m("Li Ui L")
        else:
            m("U Li Ui L")
    solveFrontSlot()

    if f2lCorrect():
        return
    else:
        f2lCornerTopNoEdge()

    if not f2lCorrect():
        raise Exception("Excepción encontrada en f2lNoEdgeOrCorner()")


# Devolverá verdadero si el f2l está completado
def isf2lDone():
    rside = a[2][0][1] == a[2][0][2] == a[2][1][1] == a[2][1][2] == a[2][2][1] == a[2][2][2]
    bside = a[5][0][0] == a[5][0][1] == a[5][0][2] == a[5][1][0] == a[5][1][1] == a[5][1][2]
    lside = a[3][0][0] == a[3][0][1] == a[3][1][0] == a[3][1][1] == a[3][2][0] == a[3][2][1]
    fside = a[1][1][0] == a[1][1][1] == a[1][1][2] == a[1][2][0] == a[1][2][1] == a[1][2][2]
    return rside and bside and lside and fside


# f2l resolverá las primeras 2 capas, verifica cada caso, luego hace un movimiento Y para verificar el siguiente
def f2l():
    pairsSolved = 0
    uMoves = 0
    while pairsSolved < 4:
        if not f2lCorrect():
            # mientras no esté correcto el f2l:
            while uMoves < 4:  # 4 movimientos antes de verificar casos raros
                solveFrontSlot()
                if f2lCorrect():
                    pairsSolved += 1
                    f2l_list.append("Caso Normal")
                    break
                else:
                    f2l_list.append("Escaneando")
                    uMoves += 1
                    m("U")
            if not f2lCorrect():
                if not f2lCornerInserted() and f2lEdgeInserted():
                    f2l_list.append("Caso raro 1")
                    f2lEdgeNoCorner()
                    pairsSolved += 1
                elif not f2lEdgeInserted() and f2lCornerInserted():
                    f2l_list.append("Caso raro 2")
                    f2lCornerNoEdge()
                    pairsSolved += 1
                # En este punto, no pueden estar insertados, deben estar en la U u otro lugar
                elif not f2lEdgeOnTop() and f2lCornerOnTop():
                    f2l_list.append("Caso raro 3")
                    f2lCornerTopNoEdge()
                    pairsSolved += 1
                elif f2lEdgeOnTop() and not f2lCornerOnTop():
                    f2l_list.append("Caso raro 4")
                    f2lEdgeTopNoCorner()
                    solveFrontSlot()
                    pairsSolved += 1
                elif not f2lEdgeOnTop() and not f2lCornerOnTop():
                    f2l_list.append("Caso raro 5")
                    f2lNoEdgeOrCorner()
                    pairsSolved += 1
                else:
                    raise Exception("Excepción de Caso Imposible en f2l")
        else:
            pairsSolved += 1
        f2l_list.append("Tenemos ")
        f2l_list.append(str(pairsSolved))
        uMoves = 0
        m("Y")
    assert (isf2lDone())


def fish():
    return [a[0][0][0], a[0][0][2], a[0][2][0], a[0][2][2]].count(a[0][1][1]) == 1


def sune():
    m("R U Ri U R U2 Ri")


def antisune():
    m("R U2 Ri Ui R Ui Ri")


def getfish():
    for i in range(4):
        if fish():
            return
        sune()
        if fish():
            return
        antisune()
        m("U")
    assert fish()


def bOLL():
    getfish()
    if fish():
        while a[0][0][2] != a[0][1][1]:
            m("U")
        if a[1][0][0] == a[0][1][1]:
            antisune()
        elif a[5][2][0] == a[0][1][1]:
            m("U2")
            sune()
        else:
            raise Exception("Algo salió mal")  # Something went wrong
    else:
        raise Exception("Fish no configurado")  # Fish not set up
    assert isTopSolved()


def getCornerState():
    corner0 = a[1][0][0] == a[1][1][1] and a[3][2][2] == a[3][1][1]
    corner1 = a[1][0][2] == a[1][1][1] and a[2][2][0] == a[2][1][1]
    corner2 = a[5][2][2] == a[5][1][1] and a[2][0][0] == a[2][1][1]
    corner3 = a[5][2][0] == a[5][1][1] and a[3][0][2] == a[3][1][1]
    return [corner0, corner1, corner2, corner3]


# Permuta las esquinas de la capa superior, las orienta correctamente
def permuteCorners():
    for i in range(2):
        for j in range(4):
            num = getCornerState().count(True)
            if num == 4:
                return
            if num == 1:
                index = getCornerState().index(True)
                for k in range(index):
                    m("Y")
                if a[1][0][2] == a[2][1][1]:
                    m("R2 B2 R F Ri B2 R Fi R")
                else:
                    m("Ri F Ri B2 R Fi Ri B2 R2")
                for f in range(index):
                    m("Yi")
                return
            m("U")
        m("R2 B2 R F Ri B2 R Fi R")


# Permuta los bordes de la capa superior, debe ser H, Z o U perms después de la orientación
def permuteEdges():
    if all(getEdgeState()):
        return
    if a[1][0][1] == a[5][1][1] and a[5][2][1] == a[1][1][1]:  # Permutación H
        m("R2 U2 R U2 R2 U2 R2 U2 R U2 R2")
    elif a[1][0][1] == a[2][1][1] and a[2][1][0] == a[1][1][1]:  # Permutación Z normal
        m("U Ri Ui R Ui R U R Ui Ri U R U R2 Ui Ri U")
    elif a[1][0][1] == a[3][1][1] and a[3][1][2] == a[1][1][1]:  # Permutación Z no orientada
        m("Ri Ui R Ui R U R Ui Ri U R U R2 Ui Ri U2")
    else:
        uNum = 0
        while True:
            if a[5][2][0] == a[5][2][1] == a[5][2][2]:  # la barra sólida está en la parte trasera
                if a[3][1][2] == a[1][0][0]:  # significa que tenemos que hacer un ciclo en sentido contrario a las agujas del reloj
                    m("R Ui R U R U R Ui Ri Ui R2")
                    break
                else:
                    m("R2 U R U Ri Ui Ri Ui Ri U Ri")
                    break
            else:
                m("U")
                uNum += 1
        for x in range(uNum):
            m("Ui")


def getEdgeState():
    fEdge = a[1][0][1] == a[1][1][1]
    rEdge = a[2][1][0] == a[2][1][1]
    bEdge = a[5][2][1] == a[5][1][1]
    lEdge = a[3][1][2] == a[3][1][1]
    return [fEdge, rEdge, bEdge, lEdge]


def topCorners():
    permuteCorners()
    assert all(getCornerState())


def topEdges():
    permuteEdges()
    assert all(getEdgeState())


def bPLL():
    topCorners()
    topEdges()


def isSolved():
    uside = a[0][0][0] == a[0][0][1] == a[0][0][2] == a[0][1][0] == a[0][1][1] == a[0][1][2] == a[0][2][0] == a[0][2][1] == a[0][2][2]
    fside = a[1][0][0] == a[1][0][1] == a[1][0][2] == a[1][1][0] == a[1][1][1] == a[1][1][2] == a[1][2][0] == a[1][2][1] == a[1][2][2]
    rside = a[2][0][0] == a[2][0][1] == a[2][0][2] == a[2][1][0] == a[2][1][1] == a[2][1][2] == a[2][2][0] == a[2][2][1] == a[2][2][2]
    lside = a[3][0][0] == a[3][0][1] == a[3][0][2] == a[3][1][0] == a[3][1][1] == a[3][1][2] == a[3][2][0] == a[3][2][1] == a[3][2][2]
    dside = a[4][0][0] == a[4][0][1] == a[4][0][2] == a[4][1][0] == a[4][1][1] == a[4][1][2] == a[4][2][0] == a[4][2][1] == a[4][2][2]
    bside = a[5][0][0] == a[5][0][1] == a[5][0][2] == a[5][1][0] == a[5][1][1] == a[5][1][2] == a[5][2][0] == a[5][2][1] == a[5][2][2]
    return uside and fside and rside and lside and dside and bside


def solve():
    cross()
    simplify_moves()
    step_moves_list[0] = solution_length
    f2l()
    simplify_moves()
    step_moves_list[1] = solution_length - step_moves_list[0]
    topCross()
    getfish()
    bOLL()
    simplify_moves()
    step_moves_list[2] = solution_length - \
        step_moves_list[1] - step_moves_list[0]
    bPLL()
    simplify_moves()
    step_moves_list[3] = solution_length - step_moves_list[2] - \
        step_moves_list[1] - step_moves_list[0]
    assert (isSolved())


# Realiza simulaciones de resolución, devolverá una lista con el número de 
# movimientos, cuál fue el mejor y el scramble utilizado para obtener el mejor. 
# El peor, cuál fue el peor, y el scramble utilizado para obtener el peor. 
# scimNum es el número de simulaciones a realizar, es un IntVar()
def simulation(simNum):
    global a
    bestScram = []
    worstScram = []
    best = 200
    worst = 0
    Bestnumber = 0
    WorstNumber = 0
    if simNum.get() >= 50000:
        print("No hagas más de 50,000 resoluciones a la vez")
        return
    for i in range(simNum.get()):
        a = make_cube()
        step_moves_list = [0, 0, 0, 0]
        f2l_list = []
        moves_list = []
        last_scramble = []
        scramble(25)
        solve()
        simplify_moves()
        if solution_length < best:
            best = solution_length
            bestScram = get_scramble()
            BestNumber = i
        if solution_length > worst:
            worst = solution_length
            worstScram = get_scramble()
            WorstNumber = i
    return [best, BestNumber, bestScram, worst, WorstNumber, worstScram]


################################################################################
# Abajo está todo el trabajo para la parte GUI del Resolutor de Cubos
################################################################################
# Estos son todos los globales utilizados para la GUI
root = None
frame = None
canvas = None
ScrambleLabel = None
SolutionLabel = None
SolutionNumberLabel = None
isTransparent = None
F2LNumberLabel = None
CrossNumberLabel = None
OLLNumberLabel = None
PLLNumberLabel = None
SimulateBestLabel = None
SimulateWorstLabel = None


# cubePoints son todas las coordenadas x e y para los polígonos utilizados para 
# los azulejos
def cubePoints():
    # h y w pueden cambiarse para permitir que el cubo se mueva por la pantalla
    h = 125
    w = 115
    # cara derecha
    # capa 1
    r00p = [0+w, 0+h, 0+w, 50+h, 33+w, 30+h, 33+w, -20+h]
    r01p = [33+w, -20+h, 33+w, 30+h, 66+w, 10+h, 66+w, -40+h]
    r02p = [66+w, -40+h, 66+w, 10+h, 99+w, -10+h, 99+w, -60+h]
    # capa 2
    r10p = [0+w, 50+h, 0+w, 100+h, 33+w, 80+h, 33+w, 30+h]
    r11p = [33+w, 30+h, 33+w, 80+h, 66+w, 60+h, 66+w, 10+h]
    r12p = [66+w, 10+h, 66+w, 60+h, 99+w, 40+h, 99+w, -10+h]
    # capa 3
    r20p = [0+w, 100+h, 0+w, 150+h, 33+w, 130+h, 33+w, 80+h]
    r21p = [33+w, 80+h, 33+w, 130+h, 66+w, 110+h, 66+w, 60+h]
    r22p = [66+w, 60+h, 66+w, 110+h, 99+w, 90+h, 99+w, 40+h]
    # cara izquierda (la cara izquierda será la cara delantera, sin embargo se 
    # llama l para distinguir entre izquierda y derecha)
    # capa 1
    l00p = [-66+w, -40+h, -66+w, 10+h, -99+w, -10+h, -99+w, -60+h]
    l01p = [-33+w, -20+h, -33+w, 30+h, -66+w, 10+h, -66+w, -40+h]
    l02p = [0+w, 0+h, 0+w, 50+h, -33+w, 30+h, -33+w, -20+h]
    # capa 2
    l10p = [-66+w, 10+h, -66+w, 60+h, -99+w, 40+h, -99+w, -10+h]
    l11p = [-33+w, 30+h, -33+w, 80+h, -66+w, 60+h, -66+w, 10+h]
    l12p = [0+w, 50+h, 0+w, 100+h, -33+w, 80+h, -33+w, 30+h]
    # capa 3
    l20p = [-66+w, 60+h, -66+w, 110+h, -99+w, 90+h, -99+w, 40+h]
    l21p = [-33+w, 80+h, -33+w, 130+h, -66+w, 110+h, -66+w, 60+h]
    l22p = [0+w, 100+h, 0+w, 150+h, -33+w, 130+h, -33+w, 80+h]
    # cara superior
    # capa 1
    u00p = [0+w, -75+h, -33+w, -94+h, 0+w, -111+h, 33+w, -94+h]
    u01p = [36+w, -57+h, 0+w, -75+h, 33+w, -94+h, 69+w, -76+h]
    u02p = [66+w, -40+h, 36+w, -57+h, 69+w, -76+h, 99+w, -60+h]
    # capa 2
    u10p = [-33+w, -57+h, -66+w, -77+h, -33+w, -94+h, 0+w, -75+h]
    u11p = [0+w, -38+h, -33+w, -57+h, 0+w, -75+h, 36+w, -57+h]
    u12p = [33+w, -20+h, 0+w, -38+h, 36+w, -57+h, 66+w, -40+h]
    # capa 3
    u20p = [-66+w, -40+h, -99+w, -60+h, -66+w, -77+h, -33+w, -57+h]
    u21p = [-33+w, -20+h, -66+w, -40+h, -33+w, -57+h, 0+w, -38+h]
    u22p = [0+w, 0+h, -33+w, -20+h, 0+w, -38+h, 33+w, -20+h]

    dh = h + 200
    dw = w
    # cara inferior
    # capa 1
    d00p = [0+dw, -75+dh, -33+dw, -94+dh, 0+dw, -111+dh, 33+dw, -94+dh]
    d01p = [36+dw, -57+dh, 0+dw, -75+dh, 33+dw, -94+dh, 69+dw, -76+dh]
    d02p = [66+dw, -40+dh, 36+dw, -57+dh, 69+dw, -76+dh, 99+dw, -60+dh]
    # capa 2
    d10p = [-33+dw, -57+dh, -66+dw, -77+dh, -33+dw, -94+dh, 0+dw, -75+dh]
    d11p = [0+dw, -38+dh, -33+dw, -57+dh, 0+dw, -75+dh, 36+dw, -57+dh]
    d12p = [33+dw, -20+dh, 0+dw, -38+dh, 36+dw, -57+dh, 66+dw, -40+dh]
    # capa 3
    d20p = [-66+dw, -40+dh, -99+dw, -60+dh, -66+dw, -77+dh, -33+dw, -57+dh]
    d21p = [-33+dw, -20+dh, -66+dw, -40+dh, -33+dw, -57+dh, 0+dw, -38+dh]
    d22p = [0+dw, 0+dh, -33+dw, -20+dh, 0+dw, -38+dh, 33+dw, -20+dh]

    return [[[u00p, u01p, u02p],
             [u10p, u11p, u12p],
             [u20p, u21p, u22p]],  # Cara superior

            [[l00p, l01p, l02p],
             [l10p, l11p, l12p],
             # cara delantera (se usa l para denotar la cara izquierda que muestra)
             [l20p, l21p, l22p]],

            [[r02p, r12p, r22p],
             [r01p, r11p, r21p],
             # cara derecha (diferente a otras caras porque está formateada de manera diferente)
             [r00p, r10p, r20p]],

            [[d20p, d21p, d22p],
             [d10p, d11p, d12p],
             [d00p, d01p, d02p]]]  # Cara inferior


def clickCanvas(canvas):
    global isTransparent
    isTransparent = not isTransparent
    canvas.delete(ALL)
    drawCube()


# DrawCanvas tomará el root y dibujará un nuevo canvas, también lo devolverá.
def drawCanvas(root):
    canvas = tk.Canvas(root, width=225, height=330, background='white')
    canvas.grid(row=0, column=0)
    canvas.bind("<Button-1>", lambda e: clickCanvas(canvas))
    return canvas


# Se usa para obtener la palabra para cada color, usada en drawCube(canvas)
def getColor(element):
    if element == 'B':
        return "#06F"  # Bonito tono de azul
    elif element == 'W':
        return "white"
    elif element == 'G':
        return "green"
    elif element == 'Y':
        return "yellow"
    elif element == 'O':
        return "orange"
    elif element == 'R':
        return "#D11"


# drawCube() tomará el canvas ya creado y dibujará el cubo con polígonos cuyos puntos están definidos en cubePoints()
def drawCube():
    global isTransparent, canvas
    pts = cubePoints()
    for j in range(3):
        for k in range(3):
            canvas.create_polygon(pts[3][j][k], fill=getColor(
                a[4][j][k]), outline="#000", width=2)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if isTransparent:
                    frontTiles = (i == 1) and ((j == 1 and k == 2) or (
                        j == 2 and k == 2) or (j == 2 and k == 1))
                    rightTiles = (i == 2) and ((j == 1 and k == 2) or (
                        j == 2 and k == 2) or (j == 2 and k == 1))
                    if frontTiles or rightTiles:
                        canvas.create_polygon(
                            pts[i][j][k], fill="", outline="#000", width=2)
                    else:
                        canvas.create_polygon(pts[i][j][k], fill=getColor(
                            a[i][j][k]), outline="#000", width=2)
                else:
                    canvas.create_polygon(pts[i][j][k], fill=getColor(
                        a[i][j][k]), outline="#000", width=2)


# Se usa para crear una nueva instancia de un cubo para resolver, cambia las etiquetas de scramble y solución también
def GUInewCube():
    global canvas, ScrambleLabel, SolutionLabel, SolutionNumberLabel, a, step_moves_list
    global PLLNumberLabel, F2LNumberLabel, CrossNumberLabel, OLLNumberLabel, f2l_list, moves_list
    step_moves_list = [0, 0, 0, 0]
    a = make_cube()
    f2l_list = []
    moves_list = []
    ScrambleLabel.configure(text="El scramble se mostrará aquí")
    SolutionLabel.configure(text="La solución se mostrará aquí")
    SolutionNumberLabel.configure(text=0)
    CrossNumberLabel.configure(text=step_moves_list[0])
    F2LNumberLabel.configure(text=step_moves_list[1])
    OLLNumberLabel.configure(text=step_moves_list[2])
    PLLNumberLabel.configure(text=step_moves_list[3])
    canvas.delete(ALL)
    drawCube()


# GUImakeMove se usa para hacer movimientos basados en lo que está en la 
# EntryBox. Después de hacer clic en Dibujar, redibujará el canvas con el cubo 
# actualizado
def GUImakeMove(move):
    global canvas
    if move.get() == "":
        return
    m(move.get())
    canvas.delete(ALL)
    drawCube()


# GUIScramble hará un scramble de 25 en el cubo, luego actualizará el canvas con el nuevo cubo
def GUIScramble():
    global ScrambleLabel, canvas
    scramble(25)
    ScrambleLabel.configure(text=get_scramble())
    canvas.delete(ALL)
    drawCube()


# Se usa para permitir al usuario ingresar su propio scramble en la Entry, 
# también mostrará el scramble en la etiqueta de scramble
def GUIcustomScramble(scram):
    global ScrambleLabel, canvas
    if scram.get() == "":
        ScrambleLabel.configure(text="El scramble se mostrará aquí")
        return
    scramble(scram.get())
    ScrambleLabel.configure(text=get_scramble())
    canvas.delete(ALL)
    drawCube()


# GUISolve resolverá el cubo usando la función solve, luego actualizará el 
# canvas con el cubo resuelto
def GUISolve():
    global canvas, SolutionLabel, SolutionNumberLabel, step_moves_list
    global PLLNumberLabel, F2LNumberLabel, CrossNumberLabel, OLLNumberLabel
    solve()
    SolutionLabel.configure(text=get_moves())
    SolutionNumberLabel.configure(text=solution_length)
    CrossNumberLabel.configure(text=step_moves_list[0])
    F2LNumberLabel.configure(text=step_moves_list[1])
    OLLNumberLabel.configure(text=step_moves_list[2])
    PLLNumberLabel.configure(text=step_moves_list[3])
    canvas.delete(ALL)
    drawCube()


# Esto permitirá al usuario avanzar por la solución un paso a la vez, el 
# parámetro step debe ser ya sea cross, f2l, OLL o PLL. Dependiendo de ello, 
# hará un paso diferente
def GUIsetSolve(step):
    global SolutionLabel, SolutionNumberLabel, canvas, step_moves_list
    global PLLNumberLabel, F2LNumberLabel, CrossNumberLabel, OLLNumberLabel
    if step == "cross":
        cross()
        simplify_moves()
        step_moves_list[0] = solution_length
    elif step == "f2l" or step == "F2L":
        f2l()
        simplify_moves()
        step_moves_list[1] = solution_length - step_moves_list[0]
    elif step == "OLL":
        topCross()
        getfish
        bOLL()
        simplify_moves()
        step_moves_list[2] = solution_length - \
            step_moves_list[1] - step_moves_list[0]
    elif step == "PLL":
        bPLL()
        simplify_moves()
        step_moves_list[3] = solution_length - step_moves_list[2] - \
            step_moves_list[1] - step_moves_list[0]
        assert (isSolved())

    SolutionLabel.configure(text=get_moves())
    SolutionNumberLabel.configure(text=solution_length)
    CrossNumberLabel.configure(text=step_moves_list[0])
    F2LNumberLabel.configure(text=step_moves_list[1])
    OLLNumberLabel.configure(text=step_moves_list[2])
    PLLNumberLabel.configure(text=step_moves_list[3])
    canvas.delete(ALL)
    drawCube()


# Esto se usa para copiar el string dado al portapapeles del usuario
def GUItoClipboard(word):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(word)
    r.destroy()


'''
Este era el intento de usar un temporizador para automatizar una solución, para usarlo, asegúrate de reactivar el botón e importar time
#Esto se usa para una solución lenta pero automática. Utiliza las funciones del temporizador para hacer un par de movimientos por segundo o algo así
def GUIautomateSolve():
    global canvas, a
    b = copy.deepcopy(a)
    solve()
    simplify_moves()
    a = b
    for i in moves_list:
        move(i)
        canvas.after(200, drawCube())
'''


# Esto se usa para exportar la solución y resolución a alg.cubing.net. Verificará si puede abrirse con
# Google Chrome, si no puede, intentará Firefox, de lo contrario, usará el navegador web predeterminado del sistema
def GUIexportSolve():
    sCopy = copy.deepcopy(get_scramble())
    mCopy = copy.deepcopy(get_moves())

    sCopy = str.replace(sCopy, "'", "-")
    sCopy = str.replace(sCopy, " ", "_")
    mCopy = str.replace(mCopy, "'", "-")
    mCopy = str.replace(mCopy, " ", "_")

    url = "alg.cubing.net/?setup=" + sCopy + "&alg=" + mCopy
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    firefox_path = "C:/Program Files/Mozilla Firefox/Firefox.exe"
    if os.path.exists(chrome_path):
        webbrowser.get(chrome_path + " %s").open(url)
    elif os.path.exists(firefox_path):
        webbrowser.get(firefox_path + " %s").open(url)
    else:
        webbrowser.open_new(url)


# Esto se usa para la rotación del cubo con botones. Toma un movimiento Yi o Y 
# para ser ejecutado
def GUIyRotation(given):
    global canvas
    if given == "Y" or given == "y":
        move('y')
    elif given == "Yi" or given == "Y'" or given == "yi" or given == "y'":
        move('yi')
    canvas.delete(ALL)
    drawCube()


# Esto creará una nueva GUI de Información, después de cerrarla, se ejecutará la GUI principal()
def InfoGUI():
    rt = tk.Tk()
    rt.geometry("600x140+50+50")  # tamaño del marco inicial
    rt.wm_title("Información del Resolutor de Cubos")
    # Solo permite que se ajuste la altura, no el ancho
    rt.resizable(True, True)
    InfoGUIy(rt)
    rt.mainloop()
    GUI()


# Esto se llamará dentro de InfoGUI(), creará una bonita GUI con instrucciones
def InfoGUIy(rt):
    frame = Frame(rt)
    frame.grid(row=0, column=0)
    wel = "Bienvenido al resolutor de cubos, aquí tienes algunas características:"
    instruct1 = "* Introduce tus propios movimientos, luego haz clic en 'ejecutar' para ejecutarlos"
    instruct2 = "* Haz clic en scramble para generar uno, o crea uno propio seleccionando 'scramble personalizado'"
    instruct3 = "* Haz clic en los dos botones de resolver para resolver, o resuelve paso a paso con los botones azules"
    instruct4 = "* Puedes copiar el scramble o la solución al portapapeles, o exportar a alg.cubing.net para visualizarlo"
    instruct5 = "* Ejecuta algunas simulaciones ingresando el número de scrambles a simular"
    InfoLabel = Label(frame, text=wel + "\n"+instruct1+"\n"+instruct2 +
                      "\n"+instruct3+"\n"+instruct4+"\n"+instruct5, justify=LEFT)
    InfoLabel.grid(row=0, column=0)
    InfoQuitButton = Button(frame, text="Empezar a Resolver",
                            fg="red", command=lambda: rt.destroy())
    InfoQuitButton.grid(row=1, column=0)


# Esto se usa para ejecutar simulaciones, utiliza la función de simulación. 
# Esta es la parte de la GUI para las simulaciones
def GUISimulation(simNum):
    global SimulateBestLabel, SimulateWorstLabel
    simResults = simulation(simNum)
    s = StringVar(value=simResults[2])
    GUIcustomScramble(s)
    GUISolve()
    SimulateBestLabel.configure(text=str(simResults[1] + 1) + " de " + str(
        simNum.get()) + " con " + str(solution_length) + " movimientos")
    SimulateWorstLabel.configure(text=str(simResults[4] + 1) + " de " + str(
        simNum.get()) + " con " + str(simResults[3]) + " movimientos")


# GUI es la GUI principal que se creará, llama a GUIy que en realidad hace todo 
# el trabajo para la GUI
def GUI():
    global root
    root = tk.Tk()
    root.geometry("700x600+50+50")  # tamaño del marco inicial
    root.wm_title("Resolutor de Cubos")
    # Solo permite que se ajuste la altura, no el ancho
    root.resizable(True, True)
    GUIy()
    root.mainloop()


# GUIy, después de que la GUI misma se cree con GUI(), esto creará todos los 
# botones, etiquetas, etc., y los añadirá a un marco. Este es el trabajo detrás 
# de escenas para la propia GUI.
def GUIy():
    global root, canvas, ScrambleLabel, SolutionLabel, SolutionNumberLabel, frame, isTransparent
    global PLLNumberLabel, F2LNumberLabel, CrossNumberLabel, OLLNumberLabel, SimulateBestLabel, SimulateWorstLabel

    isTransparent = False
    canvas = drawCanvas(root)
    drawCube()

    # locales
    move = StringVar(value="")
    scram = StringVar(value="Introduce el Scramble Aquí")
    simNum = IntVar()  # Número de Simulación

    # Marco para controles
    frame = Frame(root)
    frame.grid(row=0, column=1, sticky="n")

    # Marco para rotaciones del cubo
    Rframe = Frame(root)
    Rframe.grid(row=0, column=0, sticky="n")

    # fila 1 - etiqueta de bienvenida y botón de nuevo cubo
    Welcome = Label(frame, text="Bienvenido al Resolutor de Cubos").grid(
        row=1, column=0)
    NewCubeButton = Button(frame, text="Nuevo Cubo",
                           command=lambda: GUInewCube())
    NewCubeButton.grid(row=1, column=1)
    # fila 2 - etiqueta para indicar que introduzcas un movimiento para ejecutar
    EnterMove = Label(frame, text="Introduce movimiento(s):").grid(row=2, column=0)
    # fila 3 - Tiene entrada para movimientos personalizados así como botón para ejecutarlos
    MoveEntry = Entry(frame, textvariable=move).grid(row=3, column=0)
    DrawCubeButton = Button(frame, text="Ejecutar", command=lambda: GUImakeMove(
        move)).grid(row=3, column=1, sticky="w")
    # fila 4 - La etiqueta que imprimirá el scramble actual después de la generación
    ScrambleLabel = Label(frame, text="El scramble se mostrará aquí",
                          wraplength=180, justify=CENTER, height=2)
    ScrambleLabel.grid(row=4, column=0, columnspan=2)
    # fila 5 - El botón scramble para generar un nuevo scramble y copiar scramble al portapapeles
    ScrambleButton = Button(frame, text="Scramble", bg="lightgreen",
                            command=lambda: GUIScramble()).grid(row=5, column=0)
    CopyScrambleButton = Button(frame, text="Copiar Scramble", bg="#EF9",
                                command=lambda: GUItoClipboard(get_scramble())).grid(row=5, column=1)
    # fila 6 - entrada para scramble personalizado y botón para aplicar scramble personalizado al cubo
    CustomScramEntry = Entry(frame, textvariable=scram)
    CustomScramEntry.grid(row=6, column=0, sticky="w")
    CustomScramButton = Button(frame, text="Scramble Personalizado",
                               bg="lightgreen", command=lambda: GUIcustomScramble(scram))
    CustomScramButton.grid(row=6, column=1)
    # fila 7 - Solución lenta (usando temporizador para hacerlo lentamente), solución instantánea (solución rápida e instantánea), copiar solución al portapapeles
    # SolveTimerButton = Button(frame, text="Solución Lenta", bg="#D53", command = lambda: GUIautomateSolve()).grid(row=7, column=0, sticky="w", pady=5)
    SolveButton = Button(frame, text="Resolver Cubo", bg="#D53", command=lambda: GUISolve(
    )).grid(row=7, column=0)  # sticky="e" si también se usa el botón de temporizador
    CopyScrambleButton = Button(frame, text="Copiar Solución", bg="#EF9",
                                command=lambda: GUItoClipboard(get_moves())).grid(row=7, column=1)
    # fila 8 - Botones de solución para hacer pasos independientemente
    CrossButton = Button(frame, text="Cross", bg="lightblue",
                         command=lambda: GUIsetSolve("cross"))
    CrossButton.grid(row=8, column=0)
    F2LButton = Button(frame, text="F2l", bg="lightblue",
                       command=lambda: GUIsetSolve("F2L"))
    F2LButton.grid(row=8, column=0, sticky="e", padx=15)
    OLLButton = Button(frame, text="OLL", bg="lightblue",
                       command=lambda: GUIsetSolve("OLL"))
    OLLButton.grid(row=8, column=1, sticky="w")
    PLLButton = Button(frame, text="PLL", bg="lightblue",
                       command=lambda: GUIsetSolve("PLL"))
    PLLButton.grid(row=8, column=1, sticky="e", padx=30)
    # fila 9 - la etiqueta que contiene la solución que se generará
    SolutionLabel = Label(frame, text="La solución se mostrará aquí",
                          wraplength=250, justify=CENTER, height=8)
    SolutionLabel.grid(row=9, column=0, columnspan=2)
    # fila 10 - Etiquetas para el número de movimientos necesarios para resolver
    SolutionNumberInfoLabel = Label(frame, text="Número total de movimientos utilizados:")
    SolutionNumberInfoLabel.grid(row=10, column=0, sticky="e")
    SolutionNumberLabel = Label(frame, text="0")
    SolutionNumberLabel.grid(row=10, column=1, sticky="w")
    # fila 11, 12, 13, 14 - Etiquetas para el número de movimientos para los diferentes pasos
    CrossInfoLabel = Label(frame, text="Movimientos necesarios para Cross:")
    CrossInfoLabel.grid(row=11, column=0, sticky="e")
    CrossNumberLabel = Label(frame, text="0")
    CrossNumberLabel.grid(row=11, column=1, sticky="w")
    F2LInfoLabel = Label(frame, text="Movimientos necesarios para F2L:")
    F2LInfoLabel.grid(row=12, column=0, sticky="e")
    F2LNumberLabel = Label(frame, text="0")
    F2LNumberLabel.grid(row=12, column=1, sticky="w")
    OLLInfoLabel = Label(frame, text="Movimientos necesarios para OLL:")
    OLLInfoLabel.grid(row=13, column=0, sticky="e")
    OLLNumberLabel = Label(frame, text="0")
    OLLNumberLabel.grid(row=13, column=1, sticky="w")
    PLLInfoLabel = Label(frame, text="Movimientos necesarios para PLL:")
    PLLInfoLabel.grid(row=14, column=0, sticky="e")
    PLLNumberLabel = Label(frame, text="0")
    PLLNumberLabel.grid(row=14, column=1, sticky="w")
    # fila 15 - Exportando a alg.cubing.net
    ExportSolveButton = Button(
        frame, text="Exportar a alg.cubing.net", command=lambda: GUIexportSolve())
    ExportSolveButton.grid(row=15, column=0)
    # fila 16 - Simulaciones para la mejor solución
    SimulateEntry = Entry(frame, textvariable=simNum)
    SimulateEntry.grid(row=16, column=0)
    SimulateButton = Button(frame, text="Iniciar Simulaciones",
                            command=lambda: GUISimulation(simNum))
    SimulateButton.grid(row=16, column=1)
    # fila 17 - Qué mejor se encontró
    SimulateBestInfo = Label(frame, text="Mejor Simulación: ")
    SimulateBestInfo.grid(row=17, column=0)
    SimulateBestLabel = Label(frame, text="")
    SimulateBestLabel.grid(row=17, column=1, sticky="w")
    # fila 18 Qué peor se encontró
    SimulateWorstInfo = Label(frame, text="Peor Simulación: ")
    SimulateWorstInfo.grid(row=18, column=0)
    SimulateWorstLabel = Label(frame, text="")
    SimulateWorstLabel.grid(row=18, column=1)

    # En Rframe, botones para rotación
    RotationLabel = Label(Rframe, text="Usa los botones de abajo para rotar el cubo").grid(
        row=0, column=0, columnspan=2)
    YrotationButton = Button(Rframe, text="<---- Y",
                             command=lambda: GUIyRotation("Y"))
    YrotationButton.grid(row=1, column=0)
    YirotationButton = Button(Rframe, text="Y' ---->",
                              command=lambda: GUIyRotation("Yi"))
    YirotationButton.grid(row=1, column=1)


InfoGUI()
