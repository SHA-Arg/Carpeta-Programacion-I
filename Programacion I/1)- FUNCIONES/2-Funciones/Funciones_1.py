# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


def es_entero(ingreso):
    for caracter in ingreso:
        if caracter not in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True

# FUNCION QUE SOLICITA UN NUMERO ENTERO AL USUARIO


def solicitar_entero():
    '''
    la funcion solicitar_entero() solicita al usuario el ingreso de un numero entero.
    Si el usuario ingresa un numero entero, la funcion devuelve el numero ingresado.
    En caso contrario, la funcion solicita al usuario que ingrese un numero entero valido.
    '''
    while True:
        entrada = input("Ingrese un numero: ")
        if es_entero(entrada):
            return int(entrada)
        else:
            print("!#! Por favor, introduzca un número entero válido.\n")


# --------------------------------------------------------------------------------
# Prueba de la funcion 1|
numero = solicitar_entero()
print(f"\n<#> El numero ingresado es: {numero}\n")
print("--------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------
