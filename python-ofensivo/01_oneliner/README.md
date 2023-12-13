
# Ejemplos de oneliner en Python

No solo está la opción del interprete de python, también puedes utilizar la opción `-c` del comando para crear un script en línea.

Ejemplos:

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

1. **Imprimir números del 1 al 10:**
```bash
python33 -c 'print([i for i in range(1, 11)])'
```

2. **Calcular la suma de los cuadrados de los números del 1 al 5:**
```bash
python33 -c 'print(sum([i**2 for i in range(1, 6)]))'
```

3. **Listar archivos en el directorio actual:**
```bash
python33 -c 'import os; print(os.listdir("."))'
```

4. **Imprimir la fecha y hora actual:**
```bash
python33 -c 'from datetime import datetime; print(datetime.now())'
```

5. **Contar las líneas en un archivo:**
```bash
python33 -c 'print(sum(1 for line in open("archivo.txt")))'
```

6. **Invertir una cadena:**
```bash
python33 -c 'cadena = "Hola mundo"; print(cadena[::-1])'
```

7. **Generar una lista de números pares del 0 al 8:**
```bash
python33 -c 'print([i for i in range(9) if i % 2 == 0])'
```

8. **Verificar si un número es primo:**
```bash
python33 -c 'n = 11; print("Primo" if all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1 else "No primo")'
```
