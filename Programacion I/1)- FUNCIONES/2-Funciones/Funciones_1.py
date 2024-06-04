# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from Funciones_4 import es_entero


def solicitar_retornar_entero() -> int:
    while True:
        entrada = input("Ingrese un numero: ")
        entrada = int(entrada)
        if es_entero(entrada):
            return entrada
        else:
            print("!#! Por favor, introduzca un número entero válido.\n")


# Prueba de la funcion 1|
numero = solicitar_retornar_entero()
print(f"\n<#> El numero ingresado es: {numero}\n")
print("--------------------------------------------------------------------------\n")
