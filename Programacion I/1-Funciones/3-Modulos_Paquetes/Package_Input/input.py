# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from Package_Input.validate import *


def get_int(numero: int, mensaje_error: str, minimo: int, maximo: int, reintentos: int, tipo_dato: str) -> int | None:

    numero = int(input(numero))
    numero = validar_numero_entero(numero, mensaje_error, minimo,
                                   maximo, reintentos, tipo_dato)
    return numero


def get_float(numero: str, mensaje_error: str, minimo: float, maximo: float, reintentos: float, tipo_dato: str) -> float | None:
    numero = float(input(numero))
    numero = validar_numero_flotante(numero, mensaje_error, minimo,
                                     maximo, reintentos, tipo_dato)
    return numero


def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:

    ingreso = input(mensaje)
    cadena = ingreso
    cadena = validar_cadena(mensaje, mensaje_error, longitud, reintentos)
    return cadena
