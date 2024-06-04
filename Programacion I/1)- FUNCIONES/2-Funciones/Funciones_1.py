# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from Funciones_4 import es_entero


def solicitar_entero():
    """ Solicita al usuario ingresar un número entero
    Args:
        None
    Returns:
        int: El número entero ingresado por el usuario.  
    """
    while True:
        entrada = input("Ingrese un numero: ")
        if es_entero(entrada):
            return int(entrada)
        else:
            print("!#! Por favor, introduzca un número entero válido.\n")


# Prueba de la funcion 1|
numero = solicitar_entero()
print(f"\n<#> El numero ingresado es: {numero}\n")
print("--------------------------------------------------------------------------\n")
