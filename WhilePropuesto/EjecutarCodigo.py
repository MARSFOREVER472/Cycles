# EJERCICIO VARIABLE X:

# DATOS DE ENTRADA:

x = ["UNO", "DOS", "TRES"]
while x:
    x.pop(0)
    print(x)

# DATOS DE SALIDA:

# ['DOS', 'TRES']
# ['TRES']
# []

# EJERCICIO USANDO "else" Y "while":

x = 5

while x > 0:
    x -= 1
    print(x) # DATOS DE SALIDA: 4, 3, 2, 1, 0

else:
    print("EL BUCLE HA FINALIZADO!!!!")