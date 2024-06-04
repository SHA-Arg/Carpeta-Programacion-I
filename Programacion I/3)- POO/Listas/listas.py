# Declarar una lista con 5 elementos

lista = [1, 2, 3, 4, 5]

lista_de_diccionarios = [
    {"nombre": "Juan", "edad": 20}, {"nombre": "Pedro", "edad": 30}]

lista_de_listas = [[1, 2, 3], [4, 5, 6]]

lista_de_tuplas = [(1, 2), (3, 4), (5, 6)]


# Imprimir el primer elemento de la lista
print("Primer elemento de la listas: ")
print(lista[0])
print(lista_de_diccionarios[0])
print(lista_de_listas[0])
print(lista_de_tuplas[0])

# Imprimir el ultimo elemento de la lista
print("Ultimo elemento de la listas: ")
print(lista[-1])
print(lista_de_diccionarios[-1])
print(lista_de_listas[-1])
print(lista_de_tuplas[-1])


# Metodos de las listas

# Appendear un elemento a la lista
lista.append(6)
print(lista)

# Countear la cantidad de veces que se repite un elemento en la lista
print(lista.count(1))

# Extender una lista con otra lista
lista.extend([7, 8, 9])

# Indexar un elemento en la lista por su valor
print(lista.index(1))

# Insertar un elemento en la lista en una posicion especifica
lista.insert(0, 0)
print(lista)


# pop un elemento de la lista por su indice
print(lista)
print(lista.pop(3))
print(lista)

# Remover un elemento de la lista por su valor
print(lista)
lista.remove(0)
print(lista)

# Revertir la lista
print(lista)
lista.reverse()
print(lista)

# clear vaciar la lista
print(lista)
lista.clear()
print(lista)

# Sort Ordenar la lista de menor a mayor
lista = [8, 4, 3, 10, 5]
print(lista)
lista.sort()
print(lista)
