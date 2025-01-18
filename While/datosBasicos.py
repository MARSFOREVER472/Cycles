# While

# El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. 
# El código se ejecutará mientras una condición determinada se cumpla. 
# Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. 
# Llamaremos iteración a una ejecución completa del bloque de código.

#Cabe destacar que existe dos tipos de bucles, 
# los que tienen un número de iteraciones no definidas, 
# y los que tienen un número de iteraciones definidas. 
# El while estaría dentro del primer tipo. 
# Mas adelante veremos los for, que se engloban en el segundo.

# VALORES DE ENTRADA (5):

x = 5

while x > 0:
    x -= 1
    print(x)

# VALORES DE SALIDA (4, 3, 2, 1, 0):

# 4
# 3
# 2
# 1
# 0