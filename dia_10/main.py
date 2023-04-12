"""
Main de "invasión espacial" - Programa día 10
"""

import pygame
import random
import math
from pygame import mixer

# Inicializar pygame
pygame.init()


# VARIABLES PYGAME - Ajustes del juego
#  Crear pantalla
pantalla = pygame.display.set_mode(size=(1200, 900))

# Título
pygame.display.set_caption("Invasion espacial")

# Icono
icono = pygame.image.load("img/ovni.png")
pygame.display.set_icon(icono)

# Imagen de fondo
img_fondo = pygame.image.load("img/Penasolana_ajustada.jpg")

# Agregar música
mixer.music.load('sound/MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)


# VARIABLES DEL JUGADOR
# # Cargar imagen del cohete
img_jugador = pygame.image.load("img/cohete.png")
# # Ajustar posición inicial
JUGADOR_X = 568
JUGADOR_Y = 800
# # Ajustar posición con cambios
JUGADOR_X_CAMBIO = 0
JUGADOR_Y_CAMBIO = 0

# VARIABLES DE UNA LISTA DE ENEMIGOS
# # Cargar imagen del enemigo
img_enemigo = []
# # Ajustar posición inicial random
ENEMIGO_X = []
ENEMIGO_Y = []
# # Ajustar posición con cambios
ENEMIGO_X_CAMBIO = []
ENEMIGO_Y_CAMBIO = []
CANTIDAD_ENEMIGOS = 8

for e in range(CANTIDAD_ENEMIGOS):

    # VARIABLES DE UN ENEMIGO
    # # Cargar imagen del enemigo
    img_enemigo.append(pygame.image.load("img/enemigo.png"))
    # # Ajustar posición inicial random
    ENEMIGO_X.append(random.randint(0, 1136))
    ENEMIGO_Y.append(random.randint(0, 300))
    # # Ajustar posición con cambios
    ENEMIGO_X_CAMBIO.append(0.6)
    ENEMIGO_Y_CAMBIO.append(50)


# VARIABLES DE LA BALA
# # Cargar imagen del bala
img_bala = pygame.image.load("img/bala.png")
# # Ajustar posición inicial random
BALA_X = 0
BALA_Y = 810
# # Ajustar posición con cambios
BALA_X_CAMBIO = 0
BALA_Y_CAMBIO = 2
# # Ajustar visibilidad de la bala
BALA_VISIBLE = False

# VARIABLES PUNTUACIÓN, DECORACIÓN Y TEXTOS
PUNTAJE = 0

TEXTO_X = 10
TEXTO_Y = 10

FUENTE = pygame.font.Font('fonts/invaders.from.space.ttf', 32)
FUENTE2 = pygame.font.Font('fonts/game_over.ttf', 64)
# FUENTE2 = pygame.font.Font('freesansbold.ttf', 32) # Fuente que se incluye en pygame
FUENTE3 = pygame.font.Font('fonts/game_over.ttf', 256)


# FUNCIONES


def jugador(eje_x, eje_y):
    """ Función para el jugador """
    # blit es para arrojar a la pantalla
    pantalla.blit(img_jugador, (eje_x, eje_y))


def enemigo(eje_x, eje_y, ene):
    """ Función para el enemigo """
    # blit es para arrojar a la pantalla
    pantalla.blit(img_enemigo[ene], (eje_x, eje_y))


def disparar_bala(eje_x, eje_y):
    """ Función para el enemigo """
    # Necesitamos acceder a la función global de visibilidad
    global BALA_VISIBLE
    BALA_VISIBLE = True
    # blit es para arrojar a la pantalla
    # # Se le suma a los ejes el valor para que
    # # la bala quede en medio de la nave
    pantalla.blit(img_bala, (eje_x + 16, eje_y + 10))


def hay_colision(eje_x_objeto1, eje_y_objeto1, eje_x_objeto2, eje_y_objeto2):
    """ Calculo de la distancia entre dos objectos 
    en un plano de coordenadas
    mediante la mítica fórmula de los videojuegos 
    D = sqrt[(x2 - x1)*2 + (y2 - y1)*2 ]
    """

    distancia = math.sqrt(math.pow(eje_x_objeto2 - eje_x_objeto1, 2) +
                          math.pow(eje_y_objeto2 - eje_y_objeto1, 2))
    if distancia < 27:
        return True
    else:
        return False


def mostrar_puntuación(eje_x, eje_y):
    """ Mostrar puntuación """
    texto = FUENTE.render(f'R B D J T', True, (
        0, 0, 0))
    pantalla.blit(texto, (eje_x + 1000, eje_y))
    texto_2 = FUENTE2.render(f'Puntos: {PUNTAJE}', True, (0, 0, 0))
    pantalla.blit(texto_2, (eje_x, eje_y))


def texto_final():
    texto_3 = FUENTE3.render(f'GAME OVER', True, (0, 0, 0))
    pantalla.blit(texto_3, (300, 250))


# LOOP DEL JUEGO
# Es la columna vertebral del juego
# que está constantemente ejecutandose.
SE_EJECUTA = True
while SE_EJECUTA:

    # Ponemos un color al fondo de la pantalla
    pantalla.fill((205, 144, 220))
    pantalla.blit(img_fondo, (0, 0))

    # Introduccimos los eventos a iterar
    # Un evento será cualquier acción o interacción con el juego
    for evento in pygame.event.get():

        # Evento clicar al aspa para cerrar
        if evento.type == pygame.QUIT:

            SE_EJECUTA = False

        # EVENTO DE UNA TECLA PRESIONADA
        if evento.type == pygame.KEYDOWN:

            # Evento si la tecla presionada es flecha izquierda
            if evento.key == pygame.K_LEFT:
                JUGADOR_X_CAMBIO = -1

            # Evento si la tecla presionada es flecha derecha
            if evento.key == pygame.K_RIGHT:
                JUGADOR_X_CAMBIO = 1

            # Evento si la tecla presionada es espacio
            if evento.key == pygame.K_SPACE:
                sonido_disparo = mixer.Sound('sound/disparo.mp3')
                sonido_disparo.set_volume(0.3)
                sonido_disparo.play()
                if not BALA_VISIBLE:
                    BALA_X = JUGADOR_X
                    disparar_bala(BALA_X, BALA_Y)

            # Evento si la tecla presionada es Escape
            if evento.key == pygame.K_ESCAPE:

                SE_EJECUTA = False

        # EVENTO SOLTAR UNA TECLA PRESIONADA
        if evento.type == pygame.KEYUP:

            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                JUGADOR_X_CAMBIO = 0

    # APLICAR EL CAMBIO DE COORDENADAS QUE PROVOCA LAS TECLAS
    # Y CONTROL DEL MOVIMIENTO

    # JUGADOR
    JUGADOR_X += JUGADOR_X_CAMBIO

    # Controlar que el jugador no salga de la pantalla
    if JUGADOR_X <= 0:
        JUGADOR_X = 0
    if JUGADOR_X >= 1136:
        JUGADOR_X = 1136

    # ENEMIGO
    # Vamos a aplicar el cambio de coordenadas automática
    # al enemigo antes de aplicar las coordenadas del enemigo
    for e in range(CANTIDAD_ENEMIGOS):

        # Fin del juego
        if ENEMIGO_Y[e] > 745:
            for k in range(CANTIDAD_ENEMIGOS):
                ENEMIGO_Y[k] = 1500
            texto_final()
            mixer.music.stop()
            break

        ENEMIGO_X[e] += ENEMIGO_X_CAMBIO[e]

        # Controlar que el enemigo no salga de la pantalla
        if ENEMIGO_X[e] <= 0:
            ENEMIGO_X_CAMBIO[e] = 1
            ENEMIGO_Y[e] += ENEMIGO_Y_CAMBIO[e]
        elif ENEMIGO_X[e] >= 1136:
            ENEMIGO_X_CAMBIO[e] = -1
            ENEMIGO_Y[e] += ENEMIGO_Y_CAMBIO[e]

        # COLISIÓN
        colision = hay_colision(ENEMIGO_X[e], ENEMIGO_Y[e], BALA_X, BALA_Y)
        if colision:

            sonido_colision = mixer.Sound('sound/Golpe.mp3')
            sonido_colision.set_volume(0.3)
            sonido_colision.play()

            # Reiniciamos los valores de la bala
            BALA_Y = 810
            BALA_VISIBLE = False
            # Contabilizamos el enemigo muerto
            PUNTAJE += 1
            # Hacemos que reaparezca el enemigo
            ENEMIGO_X[e] = random.randint(0, 1136)
            ENEMIGO_Y[e] = random.randint(0, 300)
        # Llamamos a la función del enemigo
        enemigo(ENEMIGO_X[e], ENEMIGO_Y[e], e)

    # BALA
    if BALA_Y <= -64:
        BALA_Y = 810
        BALA_VISIBLE = False

    if BALA_VISIBLE:
        disparar_bala(BALA_X, BALA_Y)
        BALA_Y -= BALA_Y_CAMBIO

    # LLAMAR A LAS FUNCIONES

    # Llamamos a la función del jugador
    jugador(JUGADOR_X, JUGADOR_Y)

    # Llamaos a la puntuación
    mostrar_puntuación(TEXTO_X, TEXTO_Y)

    # Para que se ejecute lo anterior se necesita actualizar
    pygame.display.update()
