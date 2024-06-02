'''
-----------------------------------
#                                 #
# Nombre : Sebastian              #
# Apellido : Hereñu Amaral        #
# División: 112                   #
#                                 #
-----------------------------------

EJERCICIO:
Funciones Parte I

4|  Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.


'''
# 1| y 4| Esta función solicita al usuario ingresar un número entero y lo devuelve con validacion.

# ESTA FUNCION AYUDA A VALIDAR EL INGRESO DEL USUARIO DENTRO DE LA FUNCION solicitar_entero()


def es_entero(ingreso):
    for caracter in ingreso:
        if caracter not in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True

# FUNCION QUE SOLICITA UN NUMERO ENTERO AL USUARIO


def solicitar_entero():
    # VALIDACION DE INGRESO DE USUARIO
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


# 4| Esta función solicita al usuario ingresar un número flotante y lo devuelve.

# ESTA FUNCION AYUDA A VALIDAR EL INGRESO DEL USUARIO DENTRO DE LA FUNCION solicitar_flotante()
def es_flotante(ingreso):
    punto_ingresado = False
    for caracter in ingreso:
        if caracter == '.':
            if punto_ingresado:
                return False
            punto_ingresado = True
        elif caracter not in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True

# FUNCION QUE SOLICITA UN NUMERO FLOTANTE AL USUARIO


def solicitar_flotante():
    # VALIDACION DE INGRESO DE USUARIO
    while True:
        flotante = input("Ingrese un numero flotante: ")
        if es_flotante(flotante):
            return float(flotante)
        else:
            print("!#! Por favor, introduzca un número flotante válido.\n")


# --------------------------------------------------------------------------------
# Prueba de la funcion 2|
flotante = solicitar_flotante()
print(f"\n<#> El numero flotante ingresado es: {flotante}\n")
print("--------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------

# 4| Esta función solicita al usuario ingresar caracteres y retorna una cadena de caracteres de los ingresados.

# FUNCION QUE SOLICITA UNA CADENA DE CARACTERES AL USUARIO


def solicitar_cadena():
    # VALIDACION DE INGRESO DE USUARIO
    while True:
        cadena = input("Ingrese los caracteres que quiera:")
        if cadena != "":  # Compruebe si la entrada no está vacía.
            return cadena

        else:
            print("\n!#! Introduzca algun caracter al menos.\n")


# --------------------------------------------------------------------------------
# Prueba de la funcion 3|
cadena = solicitar_cadena()
print(f"\n<#> Los caracteres deseados.  : {cadena} \n")
print("--------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------
