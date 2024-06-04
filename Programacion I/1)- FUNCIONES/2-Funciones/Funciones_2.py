# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from Funciones_4 import es_flotante


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
