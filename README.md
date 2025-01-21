# **_Bucles while_**

- **_Anteriormente hemos visto el uso de la condición ```if``` y el ciclo ```for``` para modificar el flujo de ejecución del código._**
  
- **_A continuación veremos otra forma de hacerlo con el ciclo ```while```._**

### **_While_**

- **_El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. Llamaremos iteración a una ejecución completa del bloque de código._**

- **_Cabe destacar que existe dos tipos de bucles, los que tienen un número de iteraciones no definidas, y los que tienen un número de iteraciones definidas. El ```while``` estaría dentro del primer tipo. Mas adelante veremos los ```for```, que se engloban en el segundo._**

- **_En el ejemplo anterior tenemos un caso sencillo de while. Tenemos una condición x>0 y un bloque de código a ejecutar mientras dure esa condición x-=1 y print(x). Por lo tanto mientras que x sea mayor que 0, se ejecutará el código. Una vez se llega al final, se vuelve a empezar y si la condición se cumple, se ejecuta otra vez._**
  
- **_En este caso se entra al bloque de código 5 veces, hasta que en la sexta, x vale cero y por lo tanto la condición ya no se cumple. Por lo tanto el while tiene dos partes:_**

  - **_La condición que se tiene que cumplir para que se ejecute el código._**
  
  - **_El bloque de código que se ejecutará mientras la condición se cumpla._**
Ten cuidado ya que un mal uso del while puede dar lugar a bucles infinitos y problemas. Cierto es que en algún caso tal vez nos interese tener un bucle infinito, pero salvo que estemos seguros de lo que estamos haciendo, hay que tener cuidado. Imaginemos que tenemos un bucle cuya condición siempre se cumple. Por ejemplo, si ponemos True en la condición del while, siempre que se evalúe esa expresión, el resultado será True y se ejecutará el bloque de código. Una vez llegado al final del bloque, se volverá a evaluar la condición, se cumplirá, y vuelta a empezar. No te recomiendo que ejecutes el siguiente código, pero puedes intentarlo.
