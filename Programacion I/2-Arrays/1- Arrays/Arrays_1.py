# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


print("Funcion para calcular promedio de una lista de enteros")


def promedio(lista):
    suma_elementos = 0
    for i in range(len(lista)):
        suma_elementos += lista[i]
    return suma_elementos / len(lista)


# Prueba de funcion promedio() con el ingreso de una lista por el usuario.
matriz = [[0]*3 for _ in range(4)]  # Matriz de 4x3
for i in range(4):  # Filas
    for j in range(3):  # Columnas
        matriz[i][j] = int(input("Ingrese el elemento: ")
                           )  # Ingreso de elementos
print(promedio(matriz))
