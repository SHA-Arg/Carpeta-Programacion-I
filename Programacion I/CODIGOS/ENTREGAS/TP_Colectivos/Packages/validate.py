'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''


def validate_num(pedir_numero: int | float, minimo: float | int, maximo: float | int, mensaje_error: str, reintentos: int):
    contador_intentos = 0
    comprobante = False
    if pedir_numero < minimo or pedir_numero > maximo:
        while pedir_numero < minimo or pedir_numero > maximo:
            pedir_numero = input(mensaje_error)
            pedir_numero = int(pedir_numero)
            contador_intentos += 1
            if contador_intentos == reintentos:
                comprobante = False
                break
    else:
        comprobante = True
    return comprobante


def validate_str(palabra_longitud: int, mensaje_error: str, longitud: int, reintento: int):
    contador = 0
    if palabra_longitud > longitud:
        while palabra_longitud > longitud:
            palabra_ingresada = input(mensaje_error)
            palabra_longitud = len(palabra_ingresada)
            contador += 1
            if contador == reintento:
                palabra_ingresada = None
                break
    else:
        pass
    return palabra_ingresada
