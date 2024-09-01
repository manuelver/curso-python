# Solucionador de Cubo de Rubik

Solucionador de Cubo de Rubik codificado en Python.  

> Repositorio original: https://github.com/CubeLuke/Rubiks-Cube-Solver
> Codificado por <a href="https://github.com/CubeLuke">Lucas</a> y <a href="https://github.com/TomBrannan">Tom Brannan</a>

Para ejecutar el solucionador, ejecuta el archivo cube.py. La interfaz gráfica se iniciará automáticamente. Si obtienes errores, es posible que no tengas tkinter instalado. Es necesario tenerlo para ejecutar la interfaz gráfica.

### Características
Solo lee las instrucciones para ver algunas de las características incluidas en el solucionador.  
Entre las características incluidas se encuentran:  
* Scrambles generados por el usuario o por el programa  
* La capacidad de hacer movimientos personalizados  
* La capacidad de presionar el botón de resolución o cada paso de la resolución para ver el cubo resolverse paso a paso  
* La capacidad de ejecutar simulaciones con una cantidad definida por el usuario de resoluciones (ten cuidado, demasiadas podrían hacer que el programa se congele)  
* Capacidad de copiar scrambles o soluciones al portapapeles, así como verlas externamente  
* Hacer clic en el cubo 2D te permitirá ver los otros mosaicos inferiores que normalmente no son visibles  

<p align="center">
	<img src="https://cloud.githubusercontent.com/assets/10378593/5694175/4f15d546-9914-11e4-83ea-e85d91236071.png" alt ="Captura de pantalla del solucionador"/>
</p>

### Comandos Varios
Si no deseas usar la interfaz gráfica, también puedes escribir comandos de función en el intérprete. Aquí tienes algunos de los útiles:  
* print_cube()   Imprime el cubo en formato de texto  
* scramble()     Puedes proporcionar un número, un scramble en formato de cadena o nada para un scramble por defecto de 25 movimientos  
* get_scramble()  Imprime el scramble previo  
* solve()         Resolverá el cubo  
* get_moves()     Imprime la solución que se generó al usar solve()  
* simulation(num) El número proporcionado es la cantidad de resoluciones que deseas simular. Te devolverá la mejor resolución con su scramble, así como la peor resolución y su scramble.  

El solucionador en sí está basado en el método CFOP (Fridrich) para resolver el cubo. Resuelve el Cross, realiza el paso F2L, hace un OLL de 2 pasos y un PLL de 2 pasos. En cuanto a la notación, se utiliza la notación básica del mundo del cubing; sin embargo, un movimiento en sentido contrario a las agujas del reloj puede denotarse con un apóstrofe (forma estándar) o usando la letra i (denotando i para inverso).
