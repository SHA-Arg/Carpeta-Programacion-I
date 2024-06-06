# Explicacion de las funciones lambda en Python

# Las funciones lambda en Python son funciones anonimas que se definen utilizando la palabra clave lambda seguida de una lista de parametros y una expresion. Estas funciones son utiles cuando se necesita una funcion rapida y sencilla sin tener que definirla formalmente con la palabra clave def.

# Ejemplo:

# suma = lambda x, y: x + y

# print(suma(2, 3))

# Este ejemplo muestra una funcion lambda que suma dos numeros. La funcion se define utilizando la palabra clave lambda seguida de los parametros x e y, seguidos de la expresion x + y. Luego, la funcion se llama con los argumentos 2 y 3, y se imprime el resultado de la suma. En este caso, el resultado es 5.

# Sin funcion lambda:
def retornar_nota(estudiante):
    return estudiante['nota']


lista_estudiantes = [('Juan', 90),
                     ('Maria', 85),
                     ('Pedro', 88),
                     ('Ana', 92)]

lista_ordenada = sorted(lista_estudiantes, key=retornar_nota, reverse=True)
print(lista_ordenada)

# Con funcion lambda:
lista_ordenada = sorted(
    lista_estudiantes, key=lambda estudiante: estudiante[1], reverse=True)
print(lista_ordenada)

# Las funciones lambda pueden ser asignadas a variables y utilizadas como cualquier otra funcion. En el ejemplo anterior, la funcion lambda se utiliza como argumento de la funcion sorted para ordenar la lista de estudiantes por nota de forma descendente.

# lista_numeros = [1, 2, 3, 4, 5]
# retorno = lambda x: x[1]

# print(retorno(lista_numeros))

# sumar = lambda x, y: x + y
# print(sumar(2, 3))

# En este ejemplo, la funcion lambda se asigna a la variable sumar y se utiliza para sumar dos numeros. Luego, la funcion se llama con los argumentos 2 y 3, y se imprime el resultado de la suma. En este caso, el resultado es 5.

# Las funciones lambda tambien pueden ser utilizadas en funciones de orden superior, como map, filter y reduce. Estas funciones permiten aplicar una funcion a una secuencia de elementos, filtrar elementos de una secuencia y reducir una secuencia a un solo valor, respectivamente.

# Ejemplo de map con funcion lambda:
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# En este ejemplo, la funcion lambda se utiliza con la funcion map para elevar al cuadrado cada elemento de la lista de numeros. El resultado es una nueva lista con los cuadrados de los numeros originales.


# Las funciones lambda son utiles cuando se necesita una funcion simple y rapida, como en el caso de funciones de orden superior, funciones de filtrado, funciones de mapeo, etc. Sin embargo, es importante recordar que las funciones lambda solo pueden contener una expresion y no pueden contener multiples declaraciones o instrucciones.

# En resumen, las funciones lambda en Python son funciones anonimas que se definen utilizando la palabra clave lambda seguida de una lista de parametros y una expresion. Estas funciones son utiles cuando se necesita una funcion rapida y sencilla sin tener que definirla formalmente con la palabra clave def.
