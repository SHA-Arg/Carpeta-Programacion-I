'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
Arrays Unidimensionales

3°| Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

'''

# --------------------------------------------------------------------------------
print("Funcion para calcular el producto de los elementos de una lista de enteros")


def producto(lista):
    producto = 1
    for i in range(len(lista)):
        producto *= lista[i]
    return producto


# --------------------------------------------------------------------------------
# Prueba de funcion producto() con el ingreso de una lista por el usuario
matriz = [[0]*3 for _ in range(4)]
for i in range(4):
    for j in range(3):
        matriz[i][j] = int(input("Ingrese el elemento: "))
print(producto(matriz))

# --------------------------------------------------------------------------------
