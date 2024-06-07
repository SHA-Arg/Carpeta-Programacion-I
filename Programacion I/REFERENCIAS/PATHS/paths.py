'''
El path puede ser un directorio en tu sistema de archivos donde quieras guardar los archivos. Si quieres que los archivos se guarden en un directorio específico, debes pasar ese path como argumento a las funciones. Aquí tienes un ejemplo de cómo usar las funciones con un path especificado:

Ejemplo de Uso
Supongamos que deseas guardar los archivos en un directorio llamado "reportes" dentro de tu directorio de trabajo actual. Aquí te muestro cómo hacerlo:

Especifica el path del directorio:

'''


from datetime import datetime
import os

# Define el path donde se guardarán los archivos
directorio_reportes = os.path.join(os.getcwd(), "reportes")

# Crea el directorio si no existe
if not os.path.exists(directorio_reportes):
    os.makedirs(directorio_reportes)


# Usa el path al llamar a las funciones:
lista_empleados = [
    {"ID": 1, "Nombre": "Juan", "Apellido": "Pérez",
        "DNI": 12345678, "Puesto": "Gerente", "Salario": 50000},
    {"ID": 2, "Nombre": "Ana", "Apellido": "Gómez", "DNI": 87654321,
        "Puesto": "Desarrollador", "Salario": 40000},
    # Agrega más empleados si es necesario
]

# Escribir empleados en un archivo CSV
escribir_empleados(lista_empleados, os.path.join(
    directorio_reportes, "Empleados.csv"))

# Leer empleados desde un archivo CSV
empleados_leidos = leer_empleados(
    os.path.join(directorio_reportes, "Empleados.csv"))

# Generar un reporte
numero_reporte = 1
numero_reporte = reporte(empleados_leidos, numero_reporte, directorio_reportes)

# Buscar empleados por apellido y generar un informe
numero_informe = 1
numero_informe = buscar_por_apellido(
    empleados_leidos, numero_informe, directorio_reportes)


'''
Definición del path:

os.getcwd() obtiene el directorio de trabajo actual.
os.path.join(os.getcwd(), "reportes") construye el path al directorio "reportes" dentro del directorio de trabajo actual.
Creación del directorio:

os.makedirs(directorio_reportes) crea el directorio si no existe.
Llamadas a las funciones:

escribir_empleados escribe el archivo "Empleados.csv" en el directorio especificado.
leer_empleados lee el archivo "Empleados.csv" desde el directorio especificado.
reporte genera un archivo de reporte en el directorio especificado.
buscar_por_apellido genera un archivo de informe en el directorio especificado.
'''


def escribir_empleados(lista_empleados: list[dict], path: str):
    with open(path, "w") as archivo:
        archivo.write("ID,Nombre,Apellido,DNI,Salario,Puesto\n")
        for empleado in lista_empleados:
            registro = f'{empleado["ID"]},{empleado["Nombre"]},{empleado["Apellido"]},{
                empleado["DNI"]},{empleado["Puesto"]},{empleado["Salario"]}\n'
            archivo.write(registro)


def leer_empleados(path: str) -> list[dict]:
    lista_empleados = []
    with open(path, "r") as archivo:
        archivo.readline()  # Leer la cabecera
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
    return lista_empleados


def reporte(lista_empleados: list[dict], numero_reporte: int, path: str):
    sueldo_maximo = int(input("Ingrese el sueldo máximo: "))
    empleados_superan_sueldo = [
        empleado for empleado in lista_empleados if empleado["Salario"] > sueldo_maximo]

    fecha_reporte = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_reporte = f"{path}/Reporte_{numero_reporte}.txt"

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


def buscar_por_apellido(lista_empleados: list[dict], numero_informe: int, path: str):
    apellido_buscado = input(
        "Ingrese el apellido del empleado que quiera buscar: ")
    empleados_apellido = [
        empleado for empleado in lista_empleados if empleado["Apellido"] == apellido_buscado]

    fecha_informe = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_informe = f"{path}/Informe_{numero_informe}.txt"

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

    print(f"Informe generado exitosamente: {nombre_informe}")

    return numero_informe


'''
Función escribir_empleados:

Agregamos un parámetro path para especificar el path del archivo.
Usamos este path al abrir el archivo.
Función leer_empleados:

Cambiamos el nombre a leer_empleados para enfatizar que retorna una lista de empleados.
Agregamos un parámetro path para especificar el path del archivo.
Usamos este path al abrir el archivo.
Devolvemos la lista de empleados en lugar de modificar una lista pasada por parámetro.
Función reporte:

Agregamos un parámetro path para especificar el path del archivo.
Usamos este path al generar el nombre del reporte.
Función buscar_por_apellido:

Agregamos un parámetro path para especificar el path del archivo.
Usamos este path al generar el nombre del informe.

'''
