# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


def fibonacci(numero: int):
    if numero < 2:
        return numero
    else:
        '''Esta linea calcula el número de Fibonacci, para el numero ingresado, restando 1 y 2, y luego sumando los resultados de llamar recursivamente a la función fibonacci para esos números, hasta que el numero sea menor que 2 y devolverá el número.'''
        return fibonacci(numero - 1) + fibonacci(numero - 2)


numero_ingresado = input(
    "Ingrese la cantidad de numeros de la sucesion de fibonacci que desea ver: ")
numero_ingresado = int(numero_ingresado)
for iteracion in range(numero_ingresado + 1):
    print(fibonacci(iteracion))
