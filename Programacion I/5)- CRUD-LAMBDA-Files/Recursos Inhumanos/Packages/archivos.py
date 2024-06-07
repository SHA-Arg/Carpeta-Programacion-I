
import json
from datetime import datetime


def escribir_empleados(lista_empleados: list[dict]):
    with open("Empleados.csv", "w") as archivo:
        archivo.write("ID,Nombre,Apellido,DNI,Salario,Puesto\n")
        for empleado in lista_empleados:
            registro = f'{empleado["ID"]},{empleado["Nombre"]},{empleado["Apellido"]},{
                empleado["DNI"]},{empleado["Puesto"]},{empleado["Salario"]}\n'
            archivo.write(registro)


def leer_empleados(lista_empleados: list[dict]):
    try:
        with open("Empleados.csv", "r") as archivo:
            archivo.readline()
            for linea in archivo:
                registro = linea.strip().split(",")
                diccionario = {
                    "ID": int(registro[0]),
                    "Nombre": registro[1],
                    "Apellido": registro[2],
                    "DNI": int(registro[3]),
                    "Puesto": registro[4],
                    "Salario": int(registro[5])
                }
                lista_empleados.append(diccionario)
    except:
        pass


def reporte(lista_empleados: list[dict], numero_reporte: int):
    sueldo_maximo = int(input("Ingrese el suelo maximo: "))
    empleados_superan_sueldo = [
        empleado for empleado in lista_empleados if empleado["Salario"] > sueldo_maximo]

    fecha_reporte = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_reporte = f"Reporte_{numero_reporte}.txt"

    with open(nombre_reporte, "w") as archivo:
        archivo.write(f"Reporte Número: {numero_reporte}\n")
        archivo.write(f"Fecha de Solicitud: {fecha_reporte}\n")
        archivo.write(f"Cantidad de Empleados que superan el sueldo {
                      sueldo_maximo} = {len(empleados_superan_sueldo)}\n")
        archivo.write("Listado de Empleados:\n")
        archivo.write("ID, Nombre, Apellido, DNI, Puesto, Salario\n")

        for empleado in empleados_superan_sueldo:
            archivo.write(f"{empleado['ID']}, {empleado['Nombre']}, {empleado['Apellido']}, {
                          empleado['DNI']}, {empleado['Puesto']}, {empleado['Salario']}\n")

        print(f"Reporte generado exitosamente: {nombre_reporte}")

    return numero_reporte + 1


def buscar_por_apellido(lista_empleados: list[dict], numero_informe: int):

    apellido_buscado = input(
        "Ingese el apellido del empleado que quiera buscar: ")
    empleados_apellido = [
        empleado for empleado in lista_empleados if empleado["Apellido"] > apellido_buscado]

    fecha_informe = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_informe = f"Informe_{numero_informe}.txt"
    with open(nombre_informe, "w") as archivo:
        archivo.write(f"Informe Número: {numero_informe}\n")
        archivo.write(f"Fecha de Solicitud: {fecha_informe}\n")
        archivo.write(f"Cantidad de Empleados con el apellido {
                      apellido_buscado}: {len(empleados_apellido)}\n")
        archivo.write("Listado de Empleados:\n")
        archivo.write("ID, Nombre, Apellido, DNI, Puesto, Salario\n")
        for empleado in empleados_apellido:
            archivo.write(f"{empleado['ID']}, {empleado['Nombre']}, {empleado['Apellido']}, {
                          empleado['DNI']}, {empleado['Puesto']}, {empleado['Salario']}\n")

    return numero_informe
