# Explicacion y ejemplos de funciones en Python
# En Python, una funcion es un bloque de codigo que realiza una tarea especifica. Las funciones se definen con la palabra clave def, seguida del nombre de la funcion y los parentesis que contienen los parametros de la funcion. Por ejemplo:
#
# def saludar():
#     print("Hola, mundo!")
#
# En este caso, la funcion saludar imprime el mensaje "Hola, mundo!". Para llamar a una funcion, simplemente escribimos su nombre seguido de parentesis. Por ejemplo:
#
# saludar()
# Output: Hola, mundo!

# Las funciones pueden tener parametros, que son valores que se pasan a la funcion cuando se llama. Por ejemplo:

def saludar(nombre):
    print(f"Hola, {nombre}!")


saludar("Juan")
# Output: Hola, Juan!

# En este caso, la funcion saludar tiene un parametro llamado nombre, que se utiliza para imprimir un saludo personalizado. Cuando se llama a la funcion, se pasa un valor al parametro nombre, que se utiliza para personalizar el saludo.

# Las funciones pueden devolver un valor utilizando la palabra clave return. Por ejemplo:


def suma(a, b):
    return a + b


resultado = suma(2, 3)
print(resultado)
# Output: 5

# En este caso, la funcion suma recibe dos parametros, a y b, y devuelve la suma de los dos valores. Cuando se llama a la funcion, se asigna el resultado a una variable llamada resultado, que luego se imprime.


def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


resultado = sumar(5, 3)
print(resultado)
# Output: 8


# Las funciones pueden tener multiples parametros y devolver multiples valores. Por ejemplo:

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division


resultados = operaciones(5, 3)
print(resultados)
# Output: (8, 2, 15, 1.6666666666666667)

# En este caso, la funcion operaciones recibe dos parametros, a y b, y devuelve cuatro valores: la suma, la resta, la multiplicacion y la division de los dos valores. Cuando se llama a la funcion, se asigna el resultado a una variable llamada resultados, que luego se imprime.


def calcular_precio(nombre_producto, cantidad, precio_unitario, descuento=0):
    precio_final = cantidad * precio_unitario * (1 - descuento)
    return nombre_producto, cantidad, precio_final


nombre, cantidad, precio = calcular_precio("manzanas", 5, 2.5, 0.1)
print(f"El precio final de {cantidad} unidades de {nombre} es: {precio}")
# Output: El precio final de 5 unidades de manzanas es: 11.25

# En este caso, la funcion calcular_precio recibe cuatro parametros: nombre_producto, cantidad, precio_unitario y descuento (este ultimo con un valor por defecto de 0). La funcion calcula el precio final de un producto teniendo en cuenta la cantidad, el precio unitario y el descuento, y devuelve el nombre del producto, la cantidad y el precio final. Cuando se llama a la funcion, se asignan los valores devueltos a las variables nombre, cantidad y precio, que luego se imprimen.


# Las funciones en Python son una herramienta poderosa que nos permite reutilizar codigo y organizar nuestro programa de manera mas eficiente. Al definir funciones con parametros y valores de retorno, podemos crear bloques de codigo que realizan tareas especificas y devuelven resultados utiles. Esto nos permite escribir codigo mas limpio, legible y facil de mantener, lo que hace que nuestro programa sea mas facil de entender y de trabajar.

# En resumen, las funciones en Python son bloques de codigo que realizan tareas especificas. Las funciones se definen con la palabra clave def, seguida del nombre de la funcion y los parentesis que contienen los parametros de la funcion. Las funciones pueden tener parametros y devolver valores utilizando la palabra clave return. Al definir funciones con parametros y va lores de retorno, podemos reutilizar codigo, organizar nuestro programa de manera mas eficiente y escribir codigo mas limpio, legible y facil de mantener.
