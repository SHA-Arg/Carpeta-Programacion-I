'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''

from Packages.planilla import *
from Packages.operaciones import *
from os import system

"""De santino fernandez, 112-1"""


def opciones():
    menu = int(input("OPCIONES: \n 1) cargar plantilla \n 2) Mostrar la recaudación de todos los coches y líneas \n 3) Calcular y mostrar recaudación por línea. \n 4) Calcular y mostrar recaudación por coche. \n 5) Calcular y mostrar la recaudación total. \n 6) Salir \n Ingrese la opcion que desee: "))
    while menu > 6 or menu < 1:
        menu = int(input("ERROR, USTED SOLO TIENE ESTAS OPCIONES: \n 1) cargar plantilla \n 2) Mostrar la recaudación de todos los coches y líneas \n 3) Calcular y mostrar recaudación por línea. \n 4) Calcular y mostrar recaudación por coche. \n 5) Calcular y mostrar la recaudación total. \n 6) Salir \n Ingrese la opcion que desee: "))
    return menu


def menu_inicial():
    planilla = crear_planilla()
    while True:
        opcion = opciones()

        match opcion:
            case 1:
                cargar_planilla(planilla)
            case 2:
                mostrar_todos_los_coches(planilla)
            case 3:
                mostrar_por_linea(planilla)
            case 4:
                mostrar_por_coche(planilla)
            case 5:
                mostrar_total(planilla)
            case _:
                system("cls")
                print("Gracias por haber usado el programa. :)")
                system("pause")
                system("cls")
                break


menu_inicial()
