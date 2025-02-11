# **_Bucles ```while```_**

- **_Anteriormente hemos visto el uso de la condición ```if``` y el ciclo ```for``` para modificar el flujo de ejecución del código._**
  
- **_A continuación veremos otra forma de hacerlo con el ciclo ```while```._**

### **_```while```_**

- **_El uso del ```while``` nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. Cuando la condición se deje de cumplir, ésta se saldrá del bucle y se continuará la ejecución normal. Llamaremos "iteración" a una ejecución completa de un bloque de código._**

- **_Cabe destacar que existen 2 tipos de bucles, los que tienen un número de iteraciones no definidas, y los que tienen un número de iteraciones definidas. El ciclo ```while``` estaría dentro del primer tipo de variable. Más adelante veremos el ciclo ```for```, en las cuáles se engloban en el segundo._**

- **_En el ejemplo anterior tenemos un caso sencillo de ```while```. Tenemos una condición ```x>0``` y un bloque de código a ejecutar mientras dure esa condición ```x-=1``` y ```print(x)```. Por lo tanto mientras que x sea mayor que 0, se ejecutará el código. Una vez se llega al final, se vuelve a empezar y si la condición se cumple, se ejecuta otra vez._**
  
- **_En este caso se entra al bloque de código 5 veces, hasta que en la sexta, ```x``` vale 0 y por lo tanto la condición ya no se cumple. Por lo tanto el ciclo ```while``` tiene 2 partes:_**

  - **_La condición que se tiene que cumplir para que se ejecute el código._**
  
  - **_El bloque de código que se ejecutará mientras la condición se cumpla._**

- **_Ten cuidado ya que un mal uso del while puede dar lugar a bucles infinitos y problemas._**
  
- **_Cierto es que en algún caso tal vez nos interese tener un bucle infinito, pero salvo que estemos seguros de lo que estamos haciendo, hay que tener cuidado._**
  
- **_Imaginemos que tenemos un bucle cualquiera cuya condición siempre se cumple._**
  
- **_Por ejemplo, si ponemos True en la condición del while, siempre que se evalúe esa expresión, el resultado será ```True``` y se ejecutará el bloque de código._**
  
- **_Una vez llegado al final del bloque, se volverá a evaluar la condición, se cumplirá, y vuelta a empezar._**
  
- **_No te recomiendo que ejecutes el siguiente código, pero puedes intentarlo._**
```
# No ejecutes esto, en serio
while True:
    print("Bucle infinito")
```
