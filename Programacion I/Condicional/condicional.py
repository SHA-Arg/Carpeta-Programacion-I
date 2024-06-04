# Condicionales en Python

# Los condicionales en Python son muy similares a los de otros lenguajes de programación. La sintaxis es la siguiente:

# if condicion:
#     # bloque de código
# elif condicion:
#     # bloque de código
# else:
#     # bloque de código

# Ejemplo:

edad = 18

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

# Operadores de comparación
# Los operadores de comparación son los siguientes:

# == Igual
# != Difer
# < Menor que
# > Mayor que
# <= Menor o igual que
# >= Mayor o igual que

# Ejemplo:

numero = 5

if numero == 5:
    print('El número es igual a 5')
elif numero != 5:
    print('El número es diferente de 5')
elif numero < 5:
    print('El número es menor que 5')

# Operadores lógicos
# Los operadores lógicos son los siguientes:

# and Y
# or O
# not NO

# Ejemplo:

numero = 5

if numero > 0 and numero < 10:
    print('El número es mayor que 0 y menor que 10')
elif numero > 0 or numero < 10:
    print('El número es mayor que 0 o menor que 10')
elif not numero > 0:
    print('El número no es mayor que 0')
else:
    print('El número no es menor que 10')

# Operadores de identidad
# Los operadores de identidad son los siguientes:

# is Es
# is not No es

# Ejemplo:

numero = int(input('Ingrese un número: '))

if numero is 5:
    print('El número es 5')
elif numero is not 5:
    print('El número no es 5')

# Operadores de pertenencia
# Los operadores de pertenencia son los siguientes:

# in En
# not in No en

# Ejemplo:

lista = [1, 2, 3, 4, 5]

if 1 in lista:
    print('El número 1 está en la lista')
elif 6 not in lista:
    print('El número 6 no está en la lista')
else:
    print('El número 6 está en la lista')

# Ejemplo de condicional anidado:

numero = int(input('Ingrese un número: '))

if numero > 0:
    if numero < 10:
        print('El número es mayor que 0 y menor que 10')
    else:
        print('El número no es menor que 10')
else:
    print('El número no es mayor que 0')

# Ejemplo de condicional con operador ternario:

# El operador ternario es una forma abreviada de escribir un condicional. Se utiliza para asignar un valor a una variable en función de una condición.
# Sintaxis: valor1 if condicion else valor2

numero = int(input('Ingrese un número: '))

mensaje = 'El número es mayor que 0' if numero > 0 else 'El número no es mayor que 0'

print(mensaje)

# Ejemplo de condicional con operador ternario anidado:

numero = int(input('Ingrese un número: '))

mensaje = 'El número es mayor que 0 y menor que 10' if numero > 0 and numero < 10 else 'El número no es mayor que 0 o no es menor que 10'

print(mensaje)
