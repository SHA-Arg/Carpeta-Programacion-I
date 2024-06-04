# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from Funciones_4 import es_cadena


def solicitar_cadena():

    while True:
        cadena = input("Ingrese los caracteres que quiera:")
        if es_cadena(cadena):
            return cadena
        else:
            print("\n!#! Introduzca algun caracter al menos.\n")


# --------------------------------------------------------------------------------
# Prueba de la funcion 3|
cadena = solicitar_cadena()
print(f"\n<#> Los caracteres deseados.  : {cadena} \n")
print("--------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------
