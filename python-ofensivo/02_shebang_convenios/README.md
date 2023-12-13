# Shebang 

Es más óptimo usar `#!/usr/bin/env python` que `#!/usr/bin/python` porque el primero busca el intérprete en el `PATH` del sistema, mientras que el segundo asume que el intérprete está en `/usr/bin/python`.

# Convenios Python

Por otro lado, el `if` siguiente es una convención para que el código que está dentro de él solo se ejecute si el script se ejecuta directamente, y no si se importa como módulo.

```python
if ___name___ == '___main___': 

    print('Soy el módulo principal')

else:

    print('No soy el módulo principal')
```

Tener en cuenta que el nombre de las variables son en minúsculas, y si son varias palabras, se separan con guiones bajos, en snake_case Por ejemplo: `nombre_de_la_variable`.

Las Constantes son en mayúsculas, y si son varias palabras, se separan con guiones bajos, en SCREAMING_SNAKE_CASE. Por ejemplo: `NOMBRE_DE_LA_CONSTANTE`.

Las Clases son en UpperCamelCase, es decir, la primera letra de cada palabra en mayúsculas. Por ejemplo: `NombreDeLaClase`.

Las funciones son en minúsculas, y si son varias palabras, se separan con guiones bajos, en lowercamelcase. Por ejemplo: `nombredelafuncion`.

Las variables privadas se nombran con un guión bajo al principio. Por ejemplo: `_variable_privada`.


