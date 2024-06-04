# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


from Package_Arrays.array_generales import *
# Funciones a. Pedir el ingreso de 10 números enteros entre -1000 y 1000.


def ingreso_numeros(numero: int):
    pass


# Funcion b. Mostrar la cantidad de números positivos y negativos.
def contar_positivos_y_negativos(numeros: list):
    positivos = 0
    negativos = 0
    for numero in numeros:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    return positivos, negativos


# Funcion c. Mostrar la sumatoria de los números pares.
def sumatoria_de_pares(numeros: list):
    suma = 0
    for numero in numeros:
        if numeros[numero] % 2 == 0:
            suma += numero
    return suma


# Funcion d. Informar el mayor de los números impares.
def mayor_numero_impar(numeros: list):
    impar_mayor = None
    for numero in numeros:
        if numero % 2 != 0:
            if impar_mayor == None or numero > impar_mayor:
                impar_mayor = numero

    return impar_mayor


# Funcion e. Listar todos los números ingresados.
def listar_numeros(numeros: list):
    for numero in numeros:
        return numero


# Funcion f. Listar todos los números pares.
def listar_numeros_pares(numeros: list):
    for numero_par in numeros:
        if numero_par % 2 == 0:
            return numero_par


# Funcion g. Listar los números de las posiciones impares.
def listar_numeros_impares(numeros: list):
    for numero_impar in numeros:
        if numero_impar % 2 != 0:
            return numero_impar


##############################################################################################
