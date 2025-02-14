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

# Vamos a analizar el ejemplo paso por paso:
# 
# El primer bucle genera números del 0 al 2, lo que corresponde a la variable i. 
# Por otro lado el segundo bucle genera también número del 0 al 2, almacenados en la variable j. 
# Al tener un bucle dentro de otro, lo que pasa es que por cada i se generan 3j's. 
# Muy importante no olvidar que al finalizar el bucle de la j, debemos resetear j=0 para que en la siguiente iteración la condición de entrada se cumpla.

# Podemos complicar las cosas aún más y tener tres bucles anidados, generando combinaciones de 3 elementos con números 0, 1 y 2. 
# En este caso tendremos desde 0,0,0 hasta 2,2,2.

# EJEMPLO:

# DATOS DE ENTRADA:

i, j, k = 0, 0, 0

while i < 3:
    while j < 3:
        while k < 3:
            print(i, j, k)
            k += 1
            j += 1
        k = 0
    i += 1
    j = 0

# DATOS DE SALIDA:

# 0 0 0
# 0 1 1
# 0 2 2
# 1 0 0
# 1 1 1
# 1 2 2
# 2 0 0
# 2 1 1
# 2 2 2