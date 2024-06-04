# Declarar

diccionario = {
    'sebastian': [1, 2, 3],
    'hereñu': [4, 5, 6],
    'amaral': [7, 8, 9]
}

# por llave (key)
print(diccionario.keys())
# por valor (value)
print(diccionario.values())
# por items (key y value)
print(diccionario.items())

# diccionario vacio
diccionario_vacio = {}

# agregar un elemento al diccionario
diccionario_vacio['sebastian'] = [5, 4, 6]
diccionario_vacio['hereñu'] = [1, 2, 3]

# eliminar un elemento del diccionario
del diccionario_vacio['sebastian']

# eliminar un elemento del diccionario sin arrojar error si no existe
diccionario_vacio.pop('hereñu')

# vaciar el diccionario
diccionario_vacio.clear()

# copiar un diccionario
diccionario_vacio_copia = diccionario_vacio.copy()

# Iterar un diccionario
for key, value in diccionario.items():
    print(key, value)

# Iterar solo las llaves
for key in diccionario:
    print(key)

# Iterar solo los valores
for value in diccionario.values():
    print(value)
