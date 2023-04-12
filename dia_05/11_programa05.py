'''
Programa día 5 - Juego del ahorcado
'''
from random import choice
import os


def clearConsole():
    # Función limpiar consola
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def palabra_aleatoria():
    # Función que guarda palabras en una lista y escoge una aleatoria con choice
    lista_palabras = ('Argentina', 'Colombia', 'Guadalupe', 'Herramientas', 'Hogar', 'Murcielago',
                      'Uruguay', 'abdomen', 'abrelatas', 'abrigo', 'abuelo', 'aburrimiento',
                      'accion', 'agridulce', 'aguila', 'aguja', 'ahorcado', 'aire',
                      'alegria', 'Alemania', 'alfabeto', 'alimento', 'alma', 'almacen',
                      'almendra', 'alto', 'altura', 'amanecer', 'amarillo', 'ambiente',
                      'ambulancia', 'amiga', 'amigo', 'amor', 'analisis', 'ancho',
                      'anciano', 'animal', 'anochecer', 'aparato', 'apartamento', 'apoyo',
                      'araña', 'arbol', 'archiduque', 'area', 'aritmetica', 'arma',
                      'arroz', 'arte', 'articulo', 'ascensor', 'asiento', 'asociacion',
                      'aspecto', 'ataque', 'atencion', 'atmosfera', 'atomo', 'atun',
                      'aumento', 'autobus', 'automovil', 'coche', 'auto', 'autopista',
                      'autor', 'autoridad', 'avance', 'avena', 'avenida', 'avion',
                      'ayer', 'ayuda', 'azul', 'año', 'babosa', 'baloncesto',
                      'bambu', 'barba', 'barco', 'barro', 'lodo', 'base',
                      'bateria', 'bebe', 'bebida', 'beneficio', 'bicho', 'bigote',
                      'billete', 'bisabuelo', 'bisnieto', 'blanco', 'boca', 'boleto',
                      'bolsa', 'bolsillo', 'bolso', 'bomberos', 'bondad', 'bosque',
                      'boton', 'bragas', 'calzon', 'brazo', 'buey', 'bufanda',
                      'bus', 'busqueda', 'caballo', 'yegua', 'cabello', 'cabeza',
                      'cable', 'cabo', 'cadera', 'calamar', 'calcetines', 'calculadora',
                      'calendario', 'calidad', 'calle', 'calor', 'calzoncillo', 'cama',
                      'camara', 'camaron', 'cambio', 'camino', 'camisa', 'camiseta',
                      'campaña', 'campo', 'cansancio', 'cantidad', 'capacidad', 'capital',
                      'cara', 'caracol', 'caracter', 'caracteristica', 'cargo', 'carne',
                      'carpeta', 'carrera', 'carretera', 'carta', 'cartera', 'casa',
                      'casco', 'caso', 'castaña', 'castaño', 'causa', 'cebada',
                      'celeste', 'celular', 'centimetro', 'cerdo', 'cerebro', 'cero',
                      'cerradura', 'cerro', 'monte', 'montaña', 'cesped', 'chaqueta',
                      'chino', 'cielo', 'cien', 'ciento', 'ciencia', 'cierre',
                      'ciervo', 'cinco', 'cine', 'cintura', 'cinturon', 'circulo',
                      'ciruela', 'ciudad', 'claridad', 'clase', 'clavel', 'clavo',
                      'clima', 'club', 'cocodrilo', 'codigo', 'codo', 'cola',
                      'colega', 'colegio', 'color', 'coma', 'comercio', 'comida',
                      'comienzo', 'comision', 'compañia', 'competencia', 'competicion',
                      'competencia', 'computadora', 'comunicacion', 'comunidad', 'concepto',
                      'conciencia', 'condicion', 'conejo', 'conexion', 'confianza', 'conflicto',
                      'congreso', 'conjunto', 'conocido', 'conocimiento', 'consecuencia', 'consejo',
                      'constitucion', 'construccion', 'consumo', 'contenido', 'control', 'corazon',
                      'cordones', 'corriente', 'corte', 'cosa', 'costa', 'creacion',
                      'crecimiento', 'cremallera', 'criatura', 'crisis', 'cuaderno', 'cuadro',
                      'cuarto', 'cuatro', 'cucaracha', 'cuello', 'cuenta', 'cuerda',
                      'cordel', 'cordon', 'cuerpo', 'cuervo', 'cuestion', 'culo',
                      'cultura', 'curiosidad', 'curso', 'dama', 'dato', 'decada',
                      'decision', 'decreto', 'dedo', 'defensa', 'demanda', 'democracia',
                      'departamento', 'deporte', 'derecha', 'derecho', 'desarrollo', 'deseo',
                      'desierto', 'despejado', 'destino', 'destruccion', 'deterioro', 'dia',
                      'diagonal', 'diario', 'diarrea', 'dibujo', 'diccionario', 'dictadura',
                      'diente', 'diez', 'diferencia', 'dinero', 'dios', 'direccion',
                      'director', 'disposición', 'documento', 'dolor', 'domingo', 'don',
                      'dormitorio', 'dos', 'doña', 'dragon', 'duda', 'economia',
                      'edad', 'edificio', 'educacion', 'efecto', 'ejemplo', 'eleccion',
                      'electricidad', 'elefante', 'elemento', 'elevador', 'empatia', 'empleo',
                      'empresa', 'encuentro', 'energia', 'enfermedad', 'enojo', 'enfado',
                      'entorno', 'entrada', 'entretenimiento', 'epoca', 'equipo', 'equivocacion',
                      'era', 'escalera', 'escritorio', 'escritura', 'escuela', 'escultura',
                      'esfera', 'esfuerzo', 'espacio', 'espalda', 'español', 'especie',
                      'espectaculo', 'espectador', 'espera', 'espinilla', 'espiritu', 'esposa',
                      'esposo', 'esquina', 'estacion', 'parada', 'estado', 'este',
                      'estilo', 'estomago', 'estrella', 'estructura', 'estruendo', 'estudio',
                      'etapa', 'existencia', 'exito', 'experiencia', 'expresion', 'extasis',
                      'exterior', 'fabrica', 'facilidad', 'falda', 'falta', 'familia',
                      'fase', 'favor', 'fecha', 'ferrocarril', 'figura', 'fin',
                      'final', 'flor', 'fondo', 'forma', 'formacion', 'formalidad',
                      'fracaso', 'frances', 'frente', 'fruta', 'fuego', 'fuerza',
                      'funcion', 'futuro', 'gafas', 'galaxia', 'galleta', 'gallina',
                      'gas', 'gaseosa', 'gato', 'gente', 'geografia', 'gluteos',
                      'gobernador', 'intendente', 'alcalde', 'gobierno', 'gorrion', 'grabado',
                      'grado', 'gramo', 'gripe', 'gris', 'grupo', 'guerra',
                      'guitarra', 'habitacion', 'halcon', 'harina', 'hermano', 'hielo',
                      'hierro', 'higado', 'hijo', 'hilo', 'historia', 'hogar',
                      'hoja', 'hombre', 'hombro', 'hongo', 'hora', 'hotel',
                      'hoy', 'hueso', 'humanidad', 'humano', 'idea', 'extranjero',
                      'imagen', 'individuo', 'informacion', 'informatica', 'informe', 'ingles',
                      'inicio', 'insecto', 'instante', 'instituto', 'intento', 'interes',
                      'interior', 'interrupcion', 'investigacion', 'izquierda', 'japones',
                      'jirafa', 'joroba', 'judias', 'guisantes', 'jueves', 'juguete',
                      'julio', 'kilo', 'kilometro', 'labio', 'lado', 'lagarto',
                      'laguna', 'lago', 'langosta', 'largo', 'longitud', 'leon',
                      'ley', 'libertad', 'libro', 'libros', 'limon', 'litro',
                      'llave', 'llero', 'lluvia', 'logro', 'lombriz', 'loro',
                      'lugar', 'luna', 'lunes', 'luz', 'madre', 'manantial',
                      'manera', 'manga', 'mano', 'manzana', 'mar', 'oceano',
                      'maravilla', 'mariposa', 'marisco', 'marron', 'cafe', 'martes',
                      'matrimonio', 'mausoleo', 'mayoria', 'mañana', 'medida', 'mediodia',
                      'mejora', 'memoria', 'mente', 'mentira', 'mercado', 'mes',
                      'mesa', 'metal', 'metalico', 'metro', 'miedo', 'miercoles',
                      'mil', 'milenio', 'milimetro', 'millon', 'ministro', 'minoria',
                      'minuto', 'modo', 'molecula', 'molusco', 'momento', 'moneda',
                      'mono', 'mosca', 'mosquito', 'movimiento', 'mueble', 'muerte',
                      'mujer', 'mundo', 'municipio', 'musculo', 'musica', 'muslo',
                      'muñeca', 'nacimiento', 'nacion', 'naranja', 'naranja', 'anaranjado',
                      'nariz', 'naturaleza', 'necesidad', 'negro', 'nieto', 'nieve',
                      'nivel', 'niño', 'noche', 'nombre', 'norma', 'norte',
                      'notas', 'noticia', 'nublado', 'nueve', 'nuez', 'numero',
                      'objetivo', 'meta', 'objeto', 'obligacion', 'obra', 'ocasion',
                      'ocho', 'oeste', 'oficina', 'oido', 'ojo', 'olfato',
                      'omnibus', 'orden', 'ordenador', 'oreja', 'organizacion', 'origen',
                      'oro', 'oveja', 'padre', 'pais', 'pajaro', 'palabra',
                      'palma', 'panel', 'pantalla', 'pantalon', 'papel', 'paraguas',
                      'parasol', 'pareja', 'parlamentario', 'congresista', 'senador', 'diputado',
                      'parlante', 'parte', 'partido', 'pasado', 'paso', 'pasto',
                      'cesped', 'pata', 'patatas', 'papas', 'paz', 'pecho',
                      'pelusa', 'pensamiento', 'pera', 'percepcion', 'periferia', 'periodico',
                      'periodismo', 'perjuicio', 'permiso', 'perro', 'persona', 'personalidad',
                      'peso', 'pez', 'pie', 'piel', 'pierna', 'pilar',
                      'pino', 'pintura', 'piscina', 'piso', 'placer', 'planeta',
                      'planta', 'plata', 'platano', 'playa', 'plomo', 'poblacion',
                      'policia', 'polilla', 'politica', 'politico', 'pomelo', 'pomo',
                      'posavasos', 'posibilidad', 'posicion', 'potencia', 'precio', 'tarifa',
                      'pregunta', 'prenda', 'presencia', 'presente', 'presidente', 'primo',
                      'principio', 'probabilidad', 'problema', 'proceso', 'produccion', 'producto',
                      'profesion', 'programa', 'progreso', 'prohibicion', 'provincia', 'proyecto',
                      'pueblo', 'puerta', 'pulpo', 'punto', 'quejido', 'rabano',
                      'raiz', 'raiz', 'origen', 'fuente', 'rana', 'raton',
                      'rata', 'rayo', 'razon', 'realidad', 'rectangulo', 'recuerdo',
                      'reduccion', 'relacion', 'religion', 'representante', 'reproduccion',
                      'resfriado', 'respuesta', 'resultado', 'retroceso', 'reunion', 'revista',
                      'rio', 'rodilla', 'rojo', 'ropa', 'rosa', 'rosado', 'ruta',
                      'sabado', 'sal', 'salchicha', 'saltamontes', 'salud', 'sandia',
                      'sangre', 'sardina', 'secreto', 'sector', 'secuencia', 'segundo',
                      'seguridad', 'seis', 'selva', 'jungla', 'semana', 'semilla',
                      'sensacion', 'sentido', 'ser', 'serie', 'serpiente', 'servicio',
                      'señor', 'señora', 'siete', 'siglo', 'significado', 'silla', 'simbolo',
                      'similitud', 'sistema', 'situacion', 'sobrino', 'sociedad', 'sol',
                      'solapa', 'cuello', 'solicitud', 'solucion', 'sombrilla', 'sonido',
                      'sorpresa', 'subterraneo, metro', 'suciedad', 'suelo', 'suerte',
                      'sugerencia', 'sujetador', 'sosten', 'superficie', 'sur',
                      'sustancia', 'susto', 'tacto', 'tallo', 'talon', 'tamaño', 'tarde',
                      'tarima', 'telefono', 'televidente', 'tema', 'temor', 'texto',
                      'tiempo', 'tierra', 'tigre', 'tio', 'tipo', 'tomate', 'tormenta',
                      'torrefacto', 'total', 'trabajo', 'trafico', 'trancar', 'transaccion',
                      'transcurso', 'transito', 'transporte', 'trasero', 'tren', 'tres',
                      'triangulo', 'trigo', 'tristeza', 'trueno', 'tulipan', 'universidad',
                      'universo', 'uno', 'uso', 'utilizacion', 'utensilio', 'uña', 'vaca',
                      'vacaciones', 'valor', 'vanidad', 'vapor', 'vaso', 'vegetal',
                      'vehiculo', 'velocidad', 'ventana', 'verano', 'verdad', 'verde',
                      'verdura', 'vez', 'via', 'vida', 'vidrio', 'viento', 'viernes',
                      'villa', 'violeta', 'violin', 'visita', 'vista', 'volumen',
                      'voz', 'vuelto, cambio', 'xilofonoGente', 'zanahoria',
                      'region', 'zapatilla', 'zapato', 'zona')

    palabra_secreta = choice(lista_palabras).lower()

    palabra_secreta = palabra_secreta.replace('á', 'a').replace('é', 'e').replace(
        'í', 'i').replace('ó', 'o').replace('ú', 'u')

    return palabra_secreta


def mostrar_guiones(palabra_secreta):
    # Recibe la palabra de la función anterior.
    # Crea los guiones y separa las letras en una lista
    clave = 0
    dic = {}
    rallitas = {}

    for i in palabra_secreta:
        clave += 1
        dic[clave] = i

        rallitas[clave] = '-'

    return dic, rallitas


def mostrar_letras_acertadas():

    cuenta_letra = 0
    for k, v in dic_letras.items():

        if v == letra_user:
            cuenta_letra += 1
            dic_guiones[k] = letra_user
        else:
            pass

    if cuenta_letra == 1:
        sing_plural = 'letra'
    else:
        sing_plural = 'letras'

    print(f'Desvelamos {cuenta_letra} {sing_plural}: ')
    print(*dic_guiones.values(), sep=' ')
    print()


def ahorcado_intentos():
    if intentos == 6:
        print("  ____")
        print(" |    |")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("_|_")
    elif intentos == 5:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |     ")
        print(" |     ")
        print("_|_")
    elif intentos == 4:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |    |")
        print(" |     ")
        print("_|_")
    elif intentos == 3:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|")
        print(" |     ")
        print("_|_")
    elif intentos == 2:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |     ")
        print("_|_")
    elif intentos == 1:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |   / ")
        print("_|_")


#  Limpiar la terminal
clearConsole()

# Mensaje bienvenida
print('\n###################')
print('JUEGO - El ahorcado')
print('###################\n')

# Escoger palabra aleatoria
secret = palabra_aleatoria()

# Extraer diccionario de guiones con el número de letras de la palabra
# Extraer diccionario con letras de la palabra con indice
dic_letras, dic_guiones = mostrar_guiones(secret)

# ############## PRUEBAS

# print(*dic_letras, sep=' ')
# print(*dic_letras.values(), sep=' ')

# Iniciar variable de INTENTOS
intentos = 8
SECRET = secret.upper()

# Instrucciones juego
print(
    f'\nTu palabra tiene {len(dic_letras)} letras y tienes {intentos} intentos para acertarla.\n¡Suerte!\n'
)

# Mostrar guiones
print(*dic_guiones.values(), sep=' ')
print()


# Pedir letra a usuario
comando = ''
# listado para letras incorrectas y acertadas
incorrectas = list()
acertadas = list()

while comando.lower() != 'salir':

    letra_user = input('Dime una letra: ')
    comando = letra_user
    # Validar letra

    # Comando salir
    if letra_user == 'salir':
        print('\n\n¡Ciao!\n')
        break

    # # Letra ya acertada
    elif letra_user in acertadas:
        print('\nEsa letra ya la acertaste primo...\n')

    elif letra_user in incorrectas:
        print('\n¡Perdiendo intentos a lo loco! ¡A lo loco!\n')
        intentos -= 1
        ahorcado_intentos()
        print('\nTe quedan {intentos} intentos\n')
    # # acierto - Desvelar letra
    elif letra_user in dic_letras.values():
        print('\n¡Ole!')
        acertadas.append(letra_user)

        # Mostrar guiones y letras acertadas
        mostrar_letras_acertadas()

    # # fallo. Restar intentos
    else:
        intentos -= 1
        incorrectas.append(letra_user)
        print(f'Lo siento, no has acertado. Te quedan {intentos} intentos\n')
        ahorcado_intentos()
        print('\nTus errores por ahora: ')
        print(*incorrectas, sep=', ')
        print()

    # Comprobación game over / Win / nuevo intento
    if intentos == 0:
        clearConsole()
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\ \t\tGAME OVER")
        print(" |   / \\")
        print("_|_")
        print(f'\n\nLa palabra era: {SECRET}\n')

        break

    # Controlar si tiene la palabra correcta
    elif '-' not in dic_guiones.values():
        clearConsole()
        print('\n\n\n\n\n\n\n\t\t\tWIN\t\t\t\n\n\n\n\n\n\n')
        print(f'La palabra era: {SECRET}\nTe sobraron {intentos} intentos\n')
        break

    # Nuevo intento
    else:
        print("¡Inténtalo de nuevo!")
