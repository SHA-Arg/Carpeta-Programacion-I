'''

----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
Arrays Unidimensionales

Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

'''

# --------------------------------------------------------------------------------
print("Funcion para calcular promedio de numeros positivos en una lista de enteros.")


def promedio_positivos(lista):
    suma_elementos = 0
    cantidad_elementos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            suma_elementos += lista[i]
            cantidad_elementos += 1
        else:
            continue
    return suma_elementos / cantidad_elementos


# Prueba de funcion promedio_positivos() con el ingreso de una lista por el usuario.
matriz = [[0]*3 for _ in range(4)]
for i in range(4):
    for j in range(3):
        matriz[i][j] = int(input("Ingrese el elemento: "))
print(promedio_positivos(matriz))


# --------------------------------------------------------------------------------
