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

3° |  Crear una función que le solicite al usuario el ingreso de una cadena y la retorna.
4° |  Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

'''

# 3° | Esta función solicita al usuario ingresar caracteres y retorna una cadena de caracteres de los ingresados.

# FUNCION QUE SOLICITA UNA CADENA DE CARACTERES AL USUARIO


def solicitar_cadena():
    # VALIDACION DE INGRESO DE USUARIO
    while True:
        cadena = input("Ingrese los caracteres que quiera:")
        if cadena != "":  # Compruebe si la entrada no está vacía.
            return cadena

        else:
            print("\n!#! Introduzca algun caracter al menos.\n")


# --------------------------------------------------------------------------------
# Prueba de la funcion 3|
cadena = solicitar_cadena()
print(f"\n<#> Los caracteres deseados.  : {cadena} \n")
print("--------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------
