'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
Arrays Unidimensionales


Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.

'''

# --------------------------------------------------------------------------------
print("Funcion para reemplazar nombres en una lista")


def reemplazar_nombres(nombres, nombre, reemplazo):
    cantidad_reemplazos = 0
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            nombres[i] = reemplazo
            cantidad_reemplazos += 1
    return cantidad_reemplazos


# Prueba de  funcion reemplazar_nombres con el ingreso de una lista por el usuario
nombres = [[0]*1 for _ in range(4)]
for i in range(4):
    nombres[i] = input("Ingrese el nombre: ")
nombre = input("Ingrese el nombre a reemplazar: ")
reemplazo = input("Ingrese el reemplazo: ")
print(reemplazar_nombres(nombres, nombre, reemplazo),
      f"El remplazos realizado fue '{nombre}' por '{reemplazo}' en la lista '{nombres}'")


# --------------------------------------------------------------------------------
