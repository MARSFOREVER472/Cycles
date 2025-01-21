# Ten cuidado ya que un mal uso del while puede dar lugar a bucles infinitos y problemas. 
# Cierto es que en algún caso tal vez nos interese tener un bucle infinito, 
# pero salvo que estemos seguros de lo que estamos haciendo, hay que tener cuidado. 
# 
# Imaginemos que tenemos un bucle cuya condición siempre se cumple. 
# Por ejemplo, si ponemos True en la condición del while, siempre que se evalúe esa expresión, 
# el resultado será True y se ejecutará el bloque de código. 
# 
# Una vez llegado al final del bloque, se volverá a evaluar la condición, se cumplirá, y vuelta a empezar. 
# No te recomiendo que ejecutes el siguiente código, pero puedes intentarlo.

# NO EJECUTES ESTO, EN SERIO:

# while true:
#     print("Bucle Infinito")

# Es posible tener un while en una sola línea, algo muy útil si el bloque que queremos ejecutar es corto. 
# En el caso de tener mas de una sentencia, las debemos separar con ;.

x = 5
while x > 0: x -=1; print(x)

# También podemos usar otro tipo de operación dentro del while, como la que se muestra a continuación. 
# En este caso tenemos una lista que mientras no este vacía, vamos eliminando su primer elemento.

x = ["ONE", "TWO", "THREE"]
while x:
    x.pop(0)
    print(x)

# SALIDA:

# ['TWO', 'THREE']
# ['THREE']
# []