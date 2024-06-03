# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


print("Funcion para calcular la posicion del valor maximo en una lista de enteros")


def maximo_posiciones(lista):
    maximo = [[0]*3 for _ in range(4)]
    posiciones = [[0]*3 for _ in range(4)]
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posiciones = i
        else:
            continue
    return posiciones


# Prueba funcion maximo_posiciones() con el ingreso de una lista por el usuario
lista = [[0]*3 for _ in range(4)]
for i in range(4):
    for j in range(3):
        lista[i][j] = int(input("Ingrese el elemento: "))
print(maximo_posiciones(lista))

# --------------------------------------------------------------------------------
