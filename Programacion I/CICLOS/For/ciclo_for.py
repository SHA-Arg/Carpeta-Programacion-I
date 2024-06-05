# Elementos iterables: listas, tuplas, conjuntos, diccionarios, cadenas de texto, rangos, etc.

lista_nombre = ['Juan', 'Pedro', 'Luis', 'Ana', 'Maria']
tupla_nota = (5, 6, 7, 8, 9)
set_departamento = {'Ventas', 'Marketing', 'Sistemas', 'RRHH', 'Contabilidad'}


# Iterar una lista
for nombre in lista_nombre:
    print(nombre)

# Iterar una tupla
for nota in tupla_nota:
    print(nota)

# Iterar un set
for departamento in set_departamento:
    print(departamento)

# Iterar un diccionario
diccionario = {
    'sebastian': [1, 2, 3],
    'hereñu': [4, 5, 6],
    'amaral': [7, 8, 9]
}

for key, value in diccionario.items():
    print(key, value)

# Iterar solo las llaves
for key in diccionario:
    print(key)

# Iterar solo los valores
for value in diccionario.values():
    print(value)

# Iterar un rango
for i in range(1, 10):
    print(i)

# Iterar un string
for letra in 'Hola Mundo':
    print(letra)

# Iterar un string con un rango
for i in range(len('Hola Mundo')):
    print(i, '->', 'Hola Mundo'[i])

# Iterar un string con un rango y un paso
for i in range(0, len('Hola Mundo'), 2):
    print(i, '->', 'Hola Mundo'[i])

# Iterar un string con un rango y un paso negativo
for i in range(len('Hola Mundo') - 1, -1, -1):
    print(i, '->', 'Hola Mundo'[i])

# variable temporal _ para indicar que no se va a utilizar
for _ in range(5):
    print('Hola Mundo')

# Iterar una lista sin enumerate y con un rango
lista_nombre = ['Juan', 'Pedro', 'Luis', 'Ana', 'Maria']

for indice in range(len(lista_nombre)):
    print(indice, '->', lista_nombre[indice])

# Iterar una lista con enumerate
for i, nombre in enumerate(lista_nombre):
    print(i, '->', nombre)

# Iterar una lista con enumerate y un rango
for i, nombre in enumerate(lista_nombre):
    print(i, '->', lista_nombre[i])

# Iterar una tupla con enumerate
tupla_nota = (5, 6, 7, 8, 9)

for i, nota in enumerate(tupla_nota):
    print(i, '->', nota)

# Iterar un set con enumerate
set_departamento = {'Ventas', 'Marketing', 'Sistemas', 'RRHH', 'Contabilidad'}

for i, departamento in enumerate(set_departamento):
    print(i, '->', departamento)

# Iterar un diccionario con enumerate
diccionario = {
    'sebastian': [1, 2, 3],
    'hereñu': [4, 5, 6],
    'amaral': [7, 8, 9]
}

for i, (key, value) in enumerate(diccionario.items()):
    print(i, '->', key, value)


# Iterar un string con enumerate
for i, letra in enumerate('Hola Mundo'):
    print(i, '->', letra)

# Iterar un string con enumerate y un rango
for i, letra in enumerate('Hola Mundo'):
    print(i, '->', 'Hola Mundo'[i])
