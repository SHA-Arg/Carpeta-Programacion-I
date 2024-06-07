
from os import system
from Packages.validar import *
from Packages.crud import *
from Packages.operaciones import *
from Packages.archivos import *


def menu():
    opciones = [
        "1-Ingrese empleado:",
        "2-Modificar empleado:",
        "3-Eliminar Empleado:",
        "4-Mostrar todos:",
        "5-Calcular salario promedio:",
        "6-Buscar Empleado por DNI:",
        "7-Ordenar Empleados:",
        "8-Reporte:",
        "9-Elija un apellido del usuario:",
        "10-Salir"
    ]

    print("+" + "-" * 50 + "+")
    print("|{:^50}|".format("MENU"))
    print("+" + "-" * 50 + "+")

    for item in opciones:
        print("| {:<48}|".format(item))
    print("+" + "-" * 50 + "+")
    return input("Elija una opcion: ")


lista_empleados = []

leer_empleados(lista_empleados)

numero_informe = 1
numero_reporte = 1

while True:
    opcion = menu()
    match opcion:
        case "1":
            validar(lista_empleados)
            escribir_empleados(lista_empleados)
            system("cls")
        case "2":
            modificar_empleado(lista_empleados)
            system("cls")
        case "3":
            eliminar_empleado(lista_empleados)
            escribir_empleados(lista_empleados)
            system("cls")
        case "4":
            mostrar_todos(lista_empleados)
        case "5":
            calcular_promedio(lista_empleados)
            system("cls")
        case "6":
            buscar_por_dni(lista_empleados)
            system("cls")
        case "7":
            ordenar_empleados(lista_empleados)
            system("cls")
        case "8":
            system("cls")
            numero_reporte = reporte(lista_empleados, numero_reporte)
            escribir_empleados(lista_empleados)
        case "9":
            numero_informe = buscar_por_apellido(
                lista_empleados, numero_informe)
            system("cls")
            system("cls")
        case "10":
            system("cls")
            print("---------------------------------")
            print("Gracias por utilizar el programa. Hasta luego.")
            system("pause")
            system("cls")
            break
