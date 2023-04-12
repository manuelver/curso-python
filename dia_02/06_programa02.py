# Comisiones del 13% son las ventas totales
# Preguntar nombre y cuanto han vendido este mes
# Output frase que incluya su nombre y el monto que le corresponde por las comisiones
  # input para preguntar y almacenar en variables
    # los ingresos serán un string y se deben transformar a float
  # Calcular el 13% multiplicando por 0.13
  # almacenar en variable redondeando a 2 decimales

# RECOGER DATOS EN VARIABLES (Y CONVERSIÓN, TODO JUNTO)
nombre = input("¿Cuál es tu nombre? ")
ventas_mes = float(input("¿Cuáles fueron tus ventas este mes? "))

# TRANSFORMAR EL STR DE VENTAS A FLOAT PARA OPERAR
# ventas_mes = ventas_mes) # DEPRECADA, LO INTRODUZCO ARRIBA

# CALCULAR LA VENTAS TOTALES E INTRODUCIR EL RESULTADO EN UNA VARIABLE CON REDONDEO
comision = round(ventas_mes * 0.13,2)


# TRANSFORMAR LOS FLOATS EN STR PARA PODER IMPRIMIR POR PANTALLA
# ventas_mes = str(ventas_mes)
# comision = str(comision)# DEPRECADA, NO ES NECESARIA LA CONVERSIÓN

# IMPRIMIR FRASE POR PANTALLA
print(f"Hola {nombre}, tus ventas de este mes fueron {ventas_mes} Euros y tu comisión fue de {comision} Euros")
