'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''

from os import system


def mostrar_todos_los_coches(planilla):
    print("Recaudacion de todos los coches: ")
    for i in range(len(planilla)):
        print(f"linea {i + 1}:", end=" ")
        for j in range(len(planilla[0])):
            aux = planilla[i][j]
            print(f"coche {j + 1}: ${aux: 5}", end=" ")
        print()
    system("pause")
    system("cls")


def mostrar_por_linea(planilla):
    print("Recaudacion por linea:")
    for i in range(len(planilla)):
        suma = 0
        for j in range(len(planilla[0])):
            suma += planilla[i][j]
        print(f"linea {i + 1}: ${suma: 5}", end=" ")
        print()
    system("pause")
    system("cls")


def mostrar_por_coche(planilla):
    print("recaudacion por coche:")
    for i in range(len(planilla[0])):
        suma = 0
        for j in range(len(planilla)):
            suma += planilla[j][i]
        print(f"coche {i + 1}: ${suma: 5}", end=" ")
        print()
    system("pause")
    system("cls")


def mostrar_total(planilla):
    suma = 0
    for i in range(len(planilla)):
        for j in range(len(planilla[0])):
            suma += planilla[i][j]
    print(f"Recaudacion Total: $ {suma}", end=" ")
    print()
    system("pause")
    system("cls")
