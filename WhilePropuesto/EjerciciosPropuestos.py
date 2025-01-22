# EJEMPLOS "while":

# ÁRBOL DE NAVIDAD EN PYTHON:

# Imprime un árbol de navidad formado con * haciendo uso del while y de la multiplicación de un entero por una cadena, 
# cuyo resultado en Python es replicar la cadena.

# DATOS DE ENTRADA:

z = 7
x = 1

while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x += 2
    z -= 1

# DATOS DE SALIDA:

#       *       
#      ***      
#     *****
#    *******
#   *********
#  ***********
# *************

# Aunque esta no sea tal vez la mejor forma de iterar una cadena 
# es un buen ejemplo para el uso del while e introducir el indexado de listas con [], 
# que veremos en otros capítulos.

# ITERAR UNA CADENA DE TEXTO EN PYTHON:

# DATOS DE ENTRADA:

text = "Python"

i = 0

while i < len(text):
    print(text[:i + 1])
    i += 1

# DATOS DE SALIDA:

# P
# Py
# Pyt
# Pyth
# Pytho
# Python

# SUCESIÓN DE FIBONACCI EN PYTHON:

# En matemáticas, la sucesión de fibonacci es una sucesión infinita de números naturales, 
# donde el siguiente es calculado sumando los dos anteriores.

# DATOS DE ENTRADA:

a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b

# DATOS DE SALIDA:

# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21