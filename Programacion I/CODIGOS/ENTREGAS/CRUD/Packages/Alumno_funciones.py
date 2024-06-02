# ----------------------  CREATE  ----------------------------------------
def crear_alumno(dni: int, nombre: str, apellido: str, nota: int) -> dict:
    diccionario_alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "nota": nota
    }
    return diccionario_alumno


# @staticmethod
# def ingresar_alumno_lista(lista_alumnos: list["Alumno"], un_alumno: "Alumno"):
#     pass


def ingresar_alumno_lista(lista_alumnos: list):
    dni = int(input('Ingrese el DNI: '))
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    nota = int(input('Ingrese la nota: '))
    alumno = crear_alumno(dni, nombre, apellido, nota)
    lista_alumnos.append(alumno)


# ----------------------  READ  ----------------------------------------

# @staticmethod
# def mostrar_todos_los_alumnos(lista_alumnos: list["Alumno"]):
#     pass

# def mostrar_un_alumno(self):
#     pass


def mostrar_todos_los_alumnos(lista_alumnos: list[dict]):
    for alumno in lista_alumnos:
        print(f'DNI: {alumno["dni"]}')
        print(f'Nombre: {alumno["nombre"]}')
        print(f'Apellido: {alumno["apellido"]}')
        print(f'Nota: {alumno["nota"]}')
        print('-------------------------')


def mostrar_un_alumno(un_alumno: dict):
    print(f'DNI: {un_alumno["dni"]}')
    print(f'Nombre: {un_alumno["nombre"]}')
    print(f'Apellido: {un_alumno["apellido"]}')
    print(f'Nota: {un_alumno["nota"]}')


# ----------------------  UPDATE  ---------------------------------------

# @staticmethod
# def modificar_alumno(lista_alumnos: list["Alumno"], dni: int):
#     pass

def modificar_alumno(lista_alumnos: list[dict], dni: int):
    lista_alumnos = []

    for alumno in lista_alumnos:
        if alumno["dni"] == dni:
            print('Ingrese los nuevos datos del alumno')
            dni = int(input('Ingrese el DNI: '))
            nombre = input('Ingrese el nombre: ')
            apellido = input('Ingrese el apellido: ')
            nota = int(input('Ingrese la nota: '))
            alumno = crear_alumno(dni, nombre, apellido, nota)
            lista_alumnos.append(alumno)
            break
    else:
        print('No se encontro el alumno')


# ----------------------  DELETE  ----------------------------------------

# @staticmethod
# def eliminar_alumno(lista_alumnos: list["Alumno"], dni: int):
#     pass


def eliminar_alumno(lista_alumnos: list[dict], dni: int):
    for alumno in lista_alumnos:
        if alumno["dni"] == dni:
            lista_alumnos.remove(alumno)
            break
    else:
        print('No se encontro el alumno')
