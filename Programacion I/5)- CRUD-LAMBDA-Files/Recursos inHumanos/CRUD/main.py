# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


from os import system
from Packages.Alumno import *
from Packages.Alumno_funciones import *


def elegir_opcion():
    opcion = input('''MENU
                1. Ingresar un empleado
                2. Modificar un empleado
                3. Eliminar un empleado
                4. Mostrar todos los empleados
                5. Salir
                Elija una opcion: ''')

    return opcion


lista_alumnos = []

while True:
    opcion = elegir_opcion()
    match opcion:
        case '1':
            pass

        case '2':
            pass
        case '4':
            system('cls')
            print('Modificar un alumno')
            pass
        case '5':
            system('cls')
            print('Eliminar un alumno')
            pass
        case '6':
            break
        case _:
            system('cls')
            print('Opcion invalida')
