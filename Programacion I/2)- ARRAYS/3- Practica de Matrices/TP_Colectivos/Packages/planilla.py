'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''

from Packages.legajo import *
from Packages.input import *
from os import system


def crear_planilla():
    planilla = [[0] * 5 for _ in range(3)]
    return planilla


def cargar_planilla(planilla):
    legajos = generar_legajos()
    legajo_ingresado = comprobar_legajos(legajos)
    print(legajo_ingresado)
    if legajo_ingresado == False:
        print("Legajo no encontrado.")
        system("pause")
        system("cls")
    else:
        linea = get_int("Ingrese la linea: ",
                        "Error. Ingrese un valor valido.", 1, 3, 3)
        coche = get_int("Ingrese el coche: ",
                        "Error. Ingrese un valor valido.", 1, 5, 3)
        recaudacion = int(input("Ingrese el importe de la recaudacion: "))
        planilla[linea-1][coche-1] += recaudacion
        print("Planilla cargada con exito.")
        system("pause")
        system("cls")
