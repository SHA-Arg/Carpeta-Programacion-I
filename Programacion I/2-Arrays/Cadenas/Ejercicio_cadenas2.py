'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------

Ejercicio 2:
Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.

'''


def indice_primera_incidencia(cadena, caracter):
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1


cadena = "Sebastian Hereñu Amaral"
caracter = "A"
print(indice_primera_incidencia(cadena, caracter))
