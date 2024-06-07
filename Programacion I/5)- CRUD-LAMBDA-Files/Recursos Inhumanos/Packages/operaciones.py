from .crud import *
from os import system


def calcular_promedio(lista_empleados: list[dict]):
    contador_salarios = 0
    cantidad_de_salarios = len(lista_empleados)
    for empleados in lista_empleados:
        contador_salarios += empleados["Salario"]
        promedio_salarios = contador_salarios / cantidad_de_salarios
        print(f"El promedio de los Salarios es: {promedio_salarios}")
        return promedio_salarios


def buscar_por_dni(lista_empleados: list[dict]):
    dni_empleados = int(input("Ingrese el DNI del empleado que desea ver: "))
    for empleado in lista_empleados:
        if empleado["DNI"] == dni_empleados:
            mostrar_empleado(empleado)


# FUNCION ORDENAR

def ordenar_lista_ascendente(lista_empleados: list[dict], key):
    n = len(lista_empleados)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_empleados[j][key] > lista_empleados[j+1][key]:
                lista_empleados[j], lista_empleados[j +
                                                    1] = lista_empleados[j+1], lista_empleados[j]


def ordenar_lista_descendente(lista_empleados: list[dict], key):
    n = len(lista_empleados)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_empleados[j][key] < lista_empleados[j+1][key]:
                lista_empleados[j], lista_empleados[j +
                                                    1] = lista_empleados[j+1], lista_empleados[j]


def ordenar_empleados(lista_empleados: list[dict]):
    while True:
        Menu = input(
            "\n1-Nombre: \n2-Apellido: \n3-Salario: \n4-Salir \nElija una opcion:")
        match Menu:
            case "1":
                decidir = input(
                    "Ingrese la opcion que desee ordenar: \n1 Ascendente: \n2 Dsescendente: ")
                match decidir:
                    case "1":
                        ordenar_lista_ascendente(lista_empleados, "Nombre")
                    case "2":
                        ordenar_lista_descendente(lista_empleados, "Nombre")
            case "2":
                decidir = input(
                    "Ingrese la opcion que desee ordenar: \n1 Ascendente: \n2 Dsescendente: ")
                match decidir:
                    case "1":
                        ordenar_lista_ascendente(lista_empleados, "Apellido")
                    case "2":
                        ordenar_lista_descendente(lista_empleados, "Apellido")
            case "3":
                decidir = input(
                    "Ingrese la opcion que desee ordenar: \n1 Ascendente: \n2 Dsescendente: ")
                match decidir:
                    case "1":
                        ordenar_lista_ascendente(lista_empleados, "Salario")
                    case "2":
                        ordenar_lista_descendente(lista_empleados, "Salario")
            case "4":
                system("cls")
                print("Opcion correcta")
                system("pause")
                system("cls")
        break
