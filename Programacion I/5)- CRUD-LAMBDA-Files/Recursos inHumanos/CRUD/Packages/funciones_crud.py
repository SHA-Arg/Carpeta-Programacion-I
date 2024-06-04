from funciones_input import solicitar_cadena, solicitar_entero
from funciones_validate import *


def ingresar_empleado(empleados, id_actual):
    if len(empleados) >= 20:
        print("No se pueden ingresar más empleados. Capacidad máxima alcanzada.")
        return id_actual

    nombre = solicitar_cadena("Ingrese el nombre: ", 20, True)
    apellido = solicitar_cadena("Ingrese el apellido: ", 20, True)
    dni = solicitar_entero("Ingrese el DNI: ", 5000000, 99999999)

    while validar_dni(dni) == False:
        print("DNI inválido. Debe ser un valor numérico entre 5000000 y 99999999.")
        dni = solicitar_entero("Ingrese el DNI: ", 5000000, 99999999)
    puesto = solicitar_cadena(
        "Ingrese el puesto (Gerente/Supervisor/Analista/Encargado/Asistente): ")
    while validar_puesto(puesto) == False:
        print("Puesto inválido. Debe ser uno de los siguientes: Gerente, Supervisor, Analista, Encargado, Asistente.")
        puesto = solicitar_cadena(
            "Ingrese el puesto (Gerente/Supervisor/Analista/Encargado/Asistente): ")
    salario = solicitar_entero("Ingrese el salario: ")
    while validar_salario(salario) == False:
        print("Salario inválido. Debe ser un valor numérico entero no menor a $234315.")
        salario = solicitar_entero("Ingrese el salario: ")

    empleados.append({
        'ID': id_actual,
        'Nombre': nombre,
        'Apellido': apellido,
        'DNI': dni,
        'Puesto': puesto,
        'Salario': salario
    })

    print(f"Empleado {nombre} {apellido} agregado con ID {id_actual}.")
    return id_actual + 1


def modificar_empleado(empleados):
    id_modificar = solicitar_entero("Ingrese el ID del empleado a modificar: ")
    for empleado in empleados:
        if empleado['ID'] == id_modificar:
            break
        else:
            empleado = print("Empleado no encontrado.")

    if not empleado:
        print("Empleado no encontrado.")
        return

    print(f"Modificando empleado {empleado['Nombre']} {empleado['Apellido']}")
    print("1. Modificar Nombre")
    print("2. Modificar Apellido")
    print("3. Modificar DNI")
    print("4. Modificar Puesto")
    print("5. Modificar Salario")
    opcion = solicitar_entero("Seleccione una opción: ", 1, 5)

    if opcion == 1:
        empleado['Nombre'] = solicitar_cadena(
            "Ingrese el nuevo nombre: ", 20, True)
    elif opcion == 2:
        empleado['Apellido'] = solicitar_cadena(
            "Ingrese el nuevo apellido: ", 20, True)
    elif opcion == 3:
        nuevo_dni = solicitar_entero(
            "Ingrese el nuevo DNI: ", 5000000, 99999999)
        while validar_dni(nuevo_dni) == False:
            print("DNI inválido.")
            nuevo_dni = solicitar_entero(
                "Ingrese el nuevo DNI: ", 5000000, 99999999)
        empleado['DNI'] = nuevo_dni
    elif opcion == 4:
        nuevo_puesto = solicitar_cadena(
            "Ingrese el nuevo puesto (Gerente/Supervisor/Analista/Encargado/Asistente): ")
        while validar_puesto(nuevo_puesto) == False:
            print("Puesto inválido.")
            nuevo_puesto = solicitar_cadena(
                "Ingrese el nuevo puesto (Gerente/Supervisor/Analista/Encargado/Asistente): ")
        empleado['Puesto'] = nuevo_puesto
    elif opcion == 5:
        nuevo_salario = solicitar_entero("Ingrese el nuevo salario: ")
        while validar_salario(nuevo_salario) == False:
            print("Salario inválido.")
            nuevo_salario = solicitar_entero("Ingrese el nuevo salario: ")
        empleado['Salario'] = nuevo_salario

    print("Datos del empleado actualizados.")


def eliminar_empleado(empleados):
    id_eliminar = solicitar_entero("Ingrese el ID del empleado a eliminar: ")
    for empleado in empleados:
        if empleado['ID'] == id_eliminar:
            break
        else:
            empleado = print("Empleado no encontrado.")

    if empleado not in empleados:
        print("Empleado no encontrado.")
        return

    empleados.remove(empleado)
    print(f"Empleado {empleado['Nombre']} {empleado['Apellido']} eliminado.")


def mostrar_todos(empleados):
    print(f"{'ID':<5} {'Nombre':<20} {'Apellido':<20} {
          'Puesto':<15} {'Salario':<10} {'DNI':<10}")
    print("-" * 80)
    for empleado in empleados:
        print(f"{empleado['ID']:<5} {empleado['Nombre']:<20} {empleado['Apellido']:<20} {
              empleado['Puesto']:<15} {empleado['Salario']:<10} {empleado['DNI']:<10}")


def calcular_salario_promedio(empleados):
    if not empleados:
        print("No hay empleados para calcular el salario promedio.")
        return
    salario_total = sum(emp['Salario'] for emp in empleados)
    promedio = salario_total / len(empleados)
    print(f"El salario promedio es: ${promedio:.2f}")


def buscar_empleado_por_dni(empleados):
    dni_buscar = solicitar_entero(
        "Ingrese el DNI del empleado a buscar: ", 5000000, 99999999)
    empleado = next(
        (emp for emp in empleados if emp['DNI'] == dni_buscar), None)

    if not empleado:
        print("Empleado no encontrado.")
        return

    print(f"Empleado encontrado: {empleado['Nombre']} {empleado['Apellido']}, Puesto: {
          empleado['Puesto']}, Salario: ${empleado['Salario']}")


def ordenar_empleados(empleados):
    print("Ordenar por:")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Salario")
    criterio = solicitar_entero("Seleccione un criterio: ", 1, 3)

    print("1. Ascendente")
    print("2. Descendente")
    orden = solicitar_entero("Seleccione el orden: ", 1, 2)

    if criterio == 1:
        clave = 'Nombre'
    elif criterio == 2:
        clave = 'Apellido'
    else:
        clave = 'Salario'

    reverso = orden == 2
    empleados.sort(key=lambda x: x[clave], reverse=reverso)
    print("Empleados ordenados.")
    mostrar_todos(empleados)
