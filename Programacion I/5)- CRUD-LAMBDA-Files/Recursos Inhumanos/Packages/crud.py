import json


# esta funcion se encarga de validar los datos ingresados por el usuario y de crear un diccionario con los datos ingresados por el usuario para luego agregarlo a la lista de empleados que se pasa como parametro a la funcion validar y se encarga de validar que el usuario no ingrese mas de 20 empleados y de preguntarle al usuario si desea ingresar otro empleado y de agregarlo a la lista de empleados que se pasa como parametro a la funcion validar y de devolver None al final de la funcion validar.
def crear_empleado(ID: int, DNI: int, Salario: int, Nombre: str, Apellido: str, Puesto: str) -> dict:
    diccionario = {
        "ID": ID,
        "DNI": DNI,
        "Salario": Salario,
        "Nombre": Nombre,
        "Apellido": Apellido,
        "Puesto": Puesto
    }
    return diccionario


def mostrar_empleado(empleado: dict):
    print("*************************************************************************")
    print(f"| {'Nombre':^15} | {'Apellido':^15} | {
          'Puesto':^15} | {'Salario':^15} |")
    print("-------------------------------------------------------------------------")

    print(f"| {empleado['Nombre']:^15} | {empleado['Apellido']:^15} | {
          empleado['Puesto']:^15} | {empleado['Salario']:^15} |")

    print("*************************************************************************")


def mostrar_todos(lista_empleados: list[dict]):
    for empleado in lista_empleados:
        mostrar_empleado(empleado)


def modificar_empleado(lista_empleados: list[dict]):
    ID_empleado = int(
        input("Ingrese el ID del empleado que quiera modificar: "))
    encontrado = False

    while True:
        opcion_modificar = input(
            """Que desea mofidicar\n1-Nombre: \n2-Apellido: \n3-DNI: \n4-Puesto: \n5-Salario: \n6-Salir\Elija una opcion: """).strip()
        for empleado in lista_empleados:
            if empleado["ID"] == ID_empleado:
                encontrado = True
                modificaciones = False
                print("Alumno encontrado")
                break

        match opcion_modificar:
            case "1":
                Nuevo_nombre = input("Ingrese el nuevo Nombre: ").capitalize()
                if Nuevo_nombre and Nuevo_nombre.isalpha() and len(Nuevo_nombre) <= 20:
                    empleado["Nombre"] = Nuevo_nombre
                    modificaciones = True
            case "2":
                Nuevo_Apellido = input(
                    "Ingrese el nuevo Apellido: ").capitalize()
                if Nuevo_Apellido and Nuevo_Apellido.isalpha() and len(Nuevo_Apellido) <= 20:
                    empleado["Apellido"] = Nuevo_Apellido
                    modificaciones = True
            case "3":
                Nuevo_DNI = int(input("Ingrese el nuevo DNI: "))
                if 5000000 < Nuevo_DNI < 99999999:
                    empleado["DNI"] = Nuevo_DNI
                    modificaciones = True
            case "4":
                Nuevo_Puesto = input("Ingrese el nuevo Puesto: ").capitalize()
                if Nuevo_Puesto in ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]:
                    empleado["Puesto"] = Nuevo_Puesto
                    modificaciones = True
            case "5":
                Nuevo_Salario = int(input("Ingrese el nuevo Salario: "))
                if Nuevo_Salario > 234315:
                    empleado["Salario"] = Nuevo_Salario
                    modificaciones = True
            case "6":
                if modificaciones:
                    print("Se realizaron modificaciones.")
                else:
                    print("No se realizaron modificaciones.")
                return
        break


def eliminar_empleado(lista_empleado: list[dict]):
    ID_del_eliminado = int(
        input("Ingrese el ID del empleado que desea eliminar: "))
    empleado_eliminado = None
    for empleado in lista_empleado:
        if empleado["ID"] == ID_del_eliminado:
            print("Se encontro al alumno")
            empleado_eliminado = empleado

    if empleado_eliminado != None:
        lista_empleado.remove(empleado_eliminado)
    try:
        with open("Bajas.json", "r") as archivo:
            lista_eliminados = json.load(archivo)
    except:
        lista_eliminados = []

    lista_eliminados.append(empleado_eliminado)

    with open("Bajas.json", "w") as archivo:
        json.dump(lista_eliminados, archivo, indent=4)

    return empleado_eliminado
