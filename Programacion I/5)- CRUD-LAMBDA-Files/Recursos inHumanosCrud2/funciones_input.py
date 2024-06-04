def solicitar_entero(mensaje, minimo=None, maximo=None):
    valor = int(input(mensaje))
    if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
        print(f"El valor debe estar entre {minimo} y {maximo}.")
    else:
        return valor


def solicitar_cadena(mensaje, longitud_maxima=None, solo_alfabetico=False):
    while True:
        cadena = input(mensaje).strip()
        if solo_alfabetico and not cadena.isalpha():
            print("La cadena debe contener solo caracteres alfabéticos.")
        elif longitud_maxima is not None and len(cadena) > longitud_maxima:
            print(f"La cadena no debe exceder los {
                  longitud_maxima} caracteres.")
        else:
            return cadena
