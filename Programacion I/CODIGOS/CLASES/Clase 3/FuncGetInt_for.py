
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    numero = input(mensaje)
    numero = int(numero)
    # Cada vez que yo valido un dato, suma una unidad mas al reintento, al llegar a la cantidad identica, se corta la ejecucion.

    for i in range(reintentos):
        # Llamo de nuevo a input aca en esta validacion.
        while numero < minimo or numero > maximo:
            numero = input(mensaje_error)
            numero = int(numero)

    return numero


dato = get_int("Ingrese un numero: ",
               "Error. Reingrese otro numero ", 1, 10, 3)
print(dato)
