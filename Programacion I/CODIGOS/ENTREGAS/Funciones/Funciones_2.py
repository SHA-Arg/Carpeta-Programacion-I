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

2|  Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
4|  Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

'''


def es_flotante(ingreso):

    punto_ingresado = False
    for caracter in ingreso:
        if caracter == '.':
            if punto_ingresado:
                punto_ingresado = True
        elif caracter not in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True


def solicitar_flotante():
    '''
    la funcion solicitar_flotante() solicita al usuario el ingreso de un numero flotante.
    Si el usuario ingresa un numero flotante, la funcion devuelve el numero ingresado.
    En caso contrario, la funcion solicita al usuario que ingrese un numero flotante valido.

    Devuelve:
    float: El numero flotante ingresado por el usuario.

    '''
    while True:
        flotante = input("Ingrese un numero flotante: ")
        if es_flotante(flotante):
            return float(flotante)
        else:
            print("!#! Por favor, introduzca un número flotante válido.\n")


# ---------------------------------------------------------------------------------------------------------------
# Prueba de la funcion 2|
flotante = solicitar_flotante()
print(f"\n<#> El numero flotante ingresado es: {flotante}\n")
print("******************************************************************************************\n")
# ---------------------------------------------------------------------------------------------------------------
