'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''

from math import *

# region Calculos


def calcular_area_rectangulo(base, altura):
    base = float(base)
    altura = float(altura)
    area = base * altura
    return area


def calcular_perimetro_rectangulo(base, altura):
    base = float(base)
    altura = float(altura)
    perimetro = 2 * (base + altura)
    return perimetro


def calcular_area_circulo(radio):
    radio = float(radio)
    area = pi * radio ** 2
    return area


def calcular_perimetro_circulo(radio):
    radio = float(radio)
    perimetro = 2 * pi * radio
    return perimetro


def calcular_area_triangulo_rectangulo(base, altura):
    base = float(base)
    altura = float(altura)
    area = (base * altura) / 2
    return area


def calcular_perimetro_triangulo_rectangulo(base, altura):
    base = float(base)
    altura = float(altura)
    hipotenusa = sqrt(base ** 2 + altura ** 2)
    perimetro = base + altura + hipotenusa
    return perimetro


# endregion
