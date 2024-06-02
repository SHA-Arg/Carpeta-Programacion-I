'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------

Enunciado:

La empresa "Recursos Inhumanos" nos ha solicitado desarrollar un software de gestión de empleados para llevar a cabo un control exhaustivo de los mismos.

Datos correspondientes a cada empleado:
ID
Nombre
Apellido
DNI
Puesto
Salario

Consideraciones:

El programa deberá gestionar una lista de hasta 20 empleados. Cada empleado será representado mediante un diccionario.
Si se alcanza el límite de 20 empleados, se deberá notificar al usuario. Solo se podrá ingresar un empleado en caso de que se efectúe una vacante nueva (o sea que se elimine uno).
Al ingresar un empleado, el ID debe ser autoincremental, comenzando en 1. Cada empleado tendrá un ID único.
El resto de los datos deberán ser ingresados por consola.

Validaciones:

Nombre y Apellido: Deben contener solo caracteres alfabéticos, ser nombres propios y no exceder los 20 caracteres. No pueden contener números ni caracteres especiales.
Salario: Debe ser un valor numérico entero no menor a $234315.
Puesto: Debe ser uno de los siguientes: “Gerente” / “Supervisor” / “Analista” / “Encargado” / “Asistente”.
DNI: Debe ser un valor numérico entre 5000000 y 99999999.

Opciones del menú:

Ingresar empleado: Pedirá los datos necesarios y dará de alta a un nuevo empleado, asignando un ID autoincremental.
Modificar empleado: Permitirá alterar cualquier dato del empleado excepto su ID. Se usará el ID para identificar al empleado a modificar. Se mostrará un submenú para seleccionar qué datos modificar. Indicando si se realizaron modificaciones o no.
Eliminar empleado: Eliminará permanentemente a un empleado de la lista original. Se pedirá el ID del empleado a eliminar.
Mostrar todos: Imprimirá por consola la información de todos los empleados en formato de tabla:

****************************************************
|    Nombre    |   Apellido   |      Puesto      |    Salario     |
—-----------------------------------------------------------
|    German    |   Scarafilo  |     Gerente      |   $500.000 |
|   Giovanni    | Lucchetta  |  Supervisor    |  $300.000 |
****************************************************

Calcular salario promedio: Calculará e imprimirá el salario promedio de todos los empleados.
Buscar empleado por DNI: Permitir al usuario buscar y mostrar la información de un empleado específico ingresando su DNI.
Ordenar empleados: Ofrecer la opción de ordenar y mostrar la lista de empleados por nombre, apellido, o salario de forma ascendente o descendente.
Salir: Terminará la ejecución del programa.

Requisitos adicionales:

El programa deberá estar correctamente modularizado, haciendo uso de módulos, paquetes y funciones propias para solicitar enteros, flotantes y cadenas, así como para las validaciones de cada uno de estos tipos de datos.
El código debe estar programado de manera eficiente y siguiendo buenas prácticas de la programación y las reglas de estilo de la cátedra.

'''
from os import system
from Packages.Alumno_funciones import *


def elegir_opcion():
    opcion = input('''MENU
                1. Ingresar un alumno
                4. Modificar un alumno
                5. Eliminar un alumno
                2. Mostrar todos los alumnos
                6. Salir
                Elija una opcion: ''')

    return opcion


lista_alumnos = []

while True:
    opcion = elegir_opcion()
    match opcion:
        case '1':
            alumno = crear_alumno(dni=int(input('Ingrese el DNI: ')), nombre=input(
                'Ingrese el nombre: '), apellido=input('Ingrese el apellido: '), nota=int(input('Ingrese la nota: ')))
            lista_alumnos.append(alumno)

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
