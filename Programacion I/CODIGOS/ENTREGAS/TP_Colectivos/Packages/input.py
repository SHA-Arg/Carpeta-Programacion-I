'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int:
    for numero_entero in range(reintentos):
        numero_entero = int(input(mensaje))
    return numero_entero


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float:
    for numero_flotante in range(reintentos):
        numero_flotante = float(input(mensaje))
    return numero_flotante


def get_string(mensaje: str, longitud: int, intentos: int) -> str | None:
    cadena = input(mensaje)

    return cadena
