# tupla

# Definir una tupla con o sin parentesis
#   tupla = 1, 2, 3, 4, 5
#   tupla = (1, 2, 3, 4, 5)


def retornar_estudiante():
    return "Sebastian", "Hereñu", 112


tupla = retornar_estudiante()
print(tupla)


# Desempaquetar una tupla en una sola linea
# opcion 1
tupla = retornar_estudiante()
nombre = tupla[0]
apellido = tupla[1]
legajo = tupla[2]

# opcion 2
nombre, apellido, legajo = retornar_estudiante()
print(nombre)


# Intercambio de valores entre variables con tuplas
a = 10
b = 20

# lineswaping en una sola linea
a, b = b, a
a, b = (20, 10)
