# "else" Y "while":

# Algo no muy corriente en otros lenguajes de programación pero si en Python, es el uso de la cláusula "else" al final del "while". 
# Podemos ver el ejemplo anterior mezclado con el else. 
# La sección de código que se encuentra dentro del else, se ejecutará cuando el bucle termine, pero solo si lo hace “por razones naturales”. 
# Es decir, si el bucle termina porque la condición se deja de cumplir, y no porque se ha hecho uso del break.

x = 5

while x > 0:
    x -= 1
    print(x)

else:
    print("EL BUCLE HA FINALIZADO!")

# Podemos ver como si el bucle termina por el break, el print() no se ejecutará. 
# Por lo tanto, se podría decir que si no hay realmente ninguna sentencia break dentro del bucle, 
# tal vez no tenga mucho sentido el uso del else, ya que un bloque de código fuera del bucle cumplirá con la misma funcionalidad.

x = 5

while True:
    x -= 1
    print(x)

    if x == 0:
        break

else:
    # EL "print" NO SE EJECUTA...
    print("FIN DEL BUCLE")