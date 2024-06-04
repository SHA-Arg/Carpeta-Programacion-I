# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


def get_numero(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    for numero in range(reintentos):
        numero = int(input(mensaje))
    while numero <= minimo or numero >= maximo:
        print(mensaje_error)
        numero = int(input(numero))

    return numero


def numeros_pares(numeros: list) -> list:
    pares = [[numeros[i] for i in range(len(numeros)) if numeros[i] % 2 == 0]]
    # for i in range(len(numeros)):
    #     if numeros[i] % 2 == 0:
    return pares


def numeros_impares(numeros: list) -> list:
    impares = [[numeros[i]
                for i in range(len(numeros)) if numeros[i] % 2 != 0]]
    return impares
