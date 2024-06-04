# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


# 5| Esta función calcula el área de un círculo. La función recibe el radio como parámetro y devuelve el área del circulo.

from Funciones_1 import solicitar_entero


def calcular_area_circulo(radio):
    area = 3.1416 * (radio ** 2)
    return area


# --------------------------------------------------------------------------------
# Prueba de la funcion 5|
print("Ingrese un numero para el radio del círculo para calcular el área. \n")
radio = solicitar_entero()
area = calcular_area_circulo(radio)
print(f"\n<#> El área del círculo es: {area} \n")
print("--------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------
