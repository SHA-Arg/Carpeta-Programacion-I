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

# En este ejemplo, la funcion lambda se utiliza con la funcion filter para filtrar los numeros pares de la lista de numeros. El resultado es una nueva lista con los numeros pares.

lista_edades = [20, 25, 30, 35, 40]
mayores_de_30 = list(filter(lambda x: x > 30, lista_edades))
print(mayores_de_30)

# En este ejemplo, la funcion lambda se utiliza con la funcion filter para filtrar las edades mayores de 30 de la lista de edades. El resultado es una nueva lista con las edades mayores de 30.

# Ejemplo de reduce con funcion lambda:


numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)

# En este ejemplo, la funcion lambda se utiliza con la funcion reduce para sumar todos los elementos de la lista de numeros. El resultado es la suma de todos los numeros.
