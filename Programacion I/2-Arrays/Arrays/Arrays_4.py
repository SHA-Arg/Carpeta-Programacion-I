# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112
# -------------------------


print("Funcion para calcular la posicion del valor maximo en una lista de enteros")


def maximo(lista):
    maximo = lista[0]
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo


# Prueba de  funcion maximo() con el ingreso de una lista por el usuario
matriz = [[0]*3 for _ in range(4)]
for i in range(4):
    for j in range(3):
        matriz[i][j] = int(input("Ingrese el elemento: "))
print(maximo(matriz))


# --------------------------------------------------------------------------------
