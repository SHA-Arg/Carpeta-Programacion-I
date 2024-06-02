'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''


def validar_numero_entero(numero: int, mensaje_error: str, minimo: int, maximo: int, reintentos: int, tipo_dato: str) -> int | None:

    while numero > maximo or numero < minimo:
        reintentos -= 1
        numero = int(input(mensaje_error))
        if reintentos < 0:
            return None
        if tipo_dato == "float":
            numero = int(numero)
        else:
            numero = int(numero)
    return numero


def validar_numero_flotante(numero: float, mensaje_error: str, minimo: float, maximo: float, reintentos: float, tipo_dato: str) -> float | None:

    while numero > maximo or numero < minimo:
        reintentos -= 1
        numero = float(input(mensaje_error))
        if reintentos < 0:
            return None
        if tipo_dato == "int":
            numero = float(numero)
        else:
            numero = float(numero)
    return numero


def validar_cadena(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:

    cadena = len(mensaje)
    while cadena > longitud:
        reintentos -= 1
        ingreso = input(mensaje_error)
        cadena = ingreso
        cadena = len(cadena)
        if reintentos == 0:
            return None
    return f"El texto ingresado es: {ingreso} y su longitud es: {cadena}"
