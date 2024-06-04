# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


from funciones_input import solicitar_cadena, solicitar_entero
from funciones_crud import ingresar_empleado, buscar_empleado_por_dni, calcular_salario_promedio, eliminar_empleado, modificar_empleado, mostrar_todos, ordenar_empleados


def menu_principal():
    empleados = []
    id_actual = 1

    while True:
        print("\nGestión de Empleados")
        print("1. Ingresar empleado")
        print("2. Modificar empleado")
        print("3. Eliminar empleado")
        print("4. Mostrar todos los empleados")
        print("5. Calcular salario promedio")
        print("6. Buscar empleado por DNI")
        print("7. Ordenar empleados")
        print("8. Salir")

        opcion = solicitar_entero("Seleccione una opción: ", 1, 8)

        if opcion == 1:
            id_actual = ingresar_empleado(empleados, id_actual)
        elif opcion == 2:
            modificar_empleado(empleados)
        elif opcion == 3:
            eliminar_empleado(empleados)
        elif opcion == 4:
            mostrar_todos(empleados)
        elif opcion == 5:
            calcular_salario_promedio(empleados)
        elif opcion == 6:
            buscar_empleado_por_dni(empleados)
        elif opcion == 7:
            ordenar_empleados(empleados)
        elif opcion == 8:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
