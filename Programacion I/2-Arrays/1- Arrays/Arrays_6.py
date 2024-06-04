# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

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
