# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


from Funciones_4 import solicitar_entero


def verificar_par_o_impar(numero):
    if numero % 2 == 0:
        print("\n<#> El numero es par \n")
    else:
        print("\n<#> El numero es impar \n")


# --------------------------------------------------------------------------------
# Prueba de la funcion 6|
print("Ingrese un numero para verificar si es par o impar. \n")
numero = solicitar_entero()
verificar_par_o_impar(numero)
print("--------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------
