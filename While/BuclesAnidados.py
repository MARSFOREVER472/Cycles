# Ya hemos visto que los bucles while tienen una condición a evaluar y un bloque de código a ejecutar. 
# Hemos visto ejemplos donde el bloque de código son operaciones sencillas como la resta -, pero podemos complicar un poco mas las cosas y meter otro bucle while dentro del primero. 
# Es algo que resulta especialmente útil si por ejemplo queremos generar permutaciones de números, es decir, si queremos generar todas las combinaciones posibles. 
# Imaginemos que queremos generar todas las combinaciones de de dos números hasta 2. 
# Es decir, 0-0, 0-1, 0-2,… hasta 2-2.

# EJEMPLO PRÁCTICO:

# PERMUTACIÓN A GENERAR:

# DATOS DE ENTRADA: 

i = 0
j = 0

while i < 3:
    while j < 3:
        print(i, j)
        j += 1
    i += 1
    j = 0

# DATOS DE SALIDA:

# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2