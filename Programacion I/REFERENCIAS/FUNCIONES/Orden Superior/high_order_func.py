# Explicacion de funciones de orden superior en Python

# Las funciones de orden superior en Python son funciones que pueden aceptar otras funciones como argumentos y/o devolver funciones como resultado. Estas funciones son utiles para abstraer la logica comun y reutilizable en funciones mas generales, lo que permite escribir codigo mas limpio y modular. Algunos ejemplos comunes de funciones de orden superior en Python son map, filter y reduce.

# Ejemplo de map con funcion lambda:

from functools import reduce

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# En este ejemplo, la funcion lambda se utiliza con la funcion map para elevar al cuadrado cada elemento de la lista de numeros. El resultado es una nueva lista con los cuadrados de los numeros originales.

lista_nombre = ['Juan', 'Maria', 'Pedro', 'Ana']
lista_mayusculas = list(map(lambda x: x.upper(), lista_nombre))
print(lista_mayusculas)

# En este ejemplo, la funcion lambda se utiliza con la funcion map para convertir a mayusculas cada elemento de la lista de nombres. El resultado es una nueva lista con los nombres en mayusculas.

# Ejemplo de filter con funcion lambda:

numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# En este ejemplo, la funcion lambda se utiliza con la funcion filter para filtrar los numeros pares de la lista de numeros. El resultado es una nueva lista con los numeros pares. En este caso, el resultado es [2, 4].

lista_edades = [20, 25, 30, 35, 40]
mayores_de_30 = list(filter(lambda x: x > 30, lista_edades))
print(mayores_de_30)

# En este ejemplo, la funcion lambda se utiliza con la funcion filter para filtrar las edades mayores de 30 de la lista de edades. El resultado es una nueva lista con las edades mayores de 30.

# Ejemplo de reduce con funcion lambda:


numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)

# En este ejemplo, la funcion lambda se utiliza con la funcion reduce para sumar todos los elementos de la lista de numeros. El resultado es la suma de todos los numeros. En este caso, el resultado es 15.

# sorted con funcion lambda

lista_estudiantes = [('Juan', 90),
                     ('Maria', 85),
                     ('Pedro', 88),
                     ('Ana', 92)]

lista_ordenada = sorted(
    lista_estudiantes, key=lambda estudiante: estudiante[1], reverse=True)
# otra forma
# lista_ordenada = sorted(lista_estudiantes, key=lambda x: x[1], reverse=True)
print(lista_ordenada)

# En este ejemplo, la funcion lambda se utiliza como argumento de la funcion sorted para ordenar la lista de estudiantes por nota de forma descendente. La funcion lambda toma cada estudiante como argumento y devuelve su nota, que se utiliza como criterio de ordenamiento. El resultado es una lista de estudiantes ordenada por nota de forma descendente.
