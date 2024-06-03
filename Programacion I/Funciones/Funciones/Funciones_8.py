'''
-----------------------------------
#                                 #
# Nombre : Sebastian              #
# Apellido : Hereñu Amaral        #
# División: 112                   #
#                                 #
-----------------------------------

EJERCICIO:
Funciones Parte I

8|  Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

'''
from Funciones_4 import solicitar_entero


def calcular_potencia(base, exponente):
    potencia = base ** exponente
    return potencia


# -----------------------------------------------
print("Ingrese un numero para la base y un numero para el exponente para calcular la potencia. \n")
print(">> Para la base. \n")
base = solicitar_entero()
print("\n>> Y el exponente. \n")
exponente = solicitar_entero()
potencia = calcular_potencia(base, exponente)
print(f"\n<#> La potencia es: {potencia} \n")

# -----------------------------------------------
