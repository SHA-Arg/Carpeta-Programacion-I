# Declarar un set con 5 elementos
# los set son hashables y no permiten elementos duplicados
set_enteros = {1, 2, 3, 4, 5}

set_de_tuplas = {(1, 2), (3, 4), (5, 6)}


# Set vacio y agregar elementos
mi_set = set()
mi_set.add(1)
mi_set.add(2)
mi_set.add(3)
mi_set.add(4)
print(mi_set)

# No permite elementos duplicados
mi_set.add(1)
print(mi_set)

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
set_lista = set(lista)
print(set_lista)


# revisar si un elemento esta en el set
pertenece = 1 in mi_set
print(pertenece)
# Otra forma
print(1 in mi_set)


# revisar si un elemento no esta en el set
print(1 not in mi_set)

# Iterar un set
for elemento in mi_set:
    print(elemento)


# Metodos de los sets

# Agregar un elemento al set
mi_set.add(5)

# Eliminar un elemento del set

mi_set.remove(5)

# Eliminar un elemento del set sin arrojar error si no existe
mi_set.discard(5)

# Vaciar el set
mi_set.clear()

# Copiar un set
mi_set_copia = mi_set.copy()

# Union de sets
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
set_union = set1.union(set2)

# Interseccion de sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_interseccion = set1.intersection(set2)

# Diferencia de sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_diferencia = set1.difference(set2)

# Diferencia simetrica de sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_diferencia_simetrica = set1.symmetric_difference(set2)

# Subset subconjunto
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5}
es_subset = set2.issubset(set1)

# Superset superconjunto
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5}
es_superset = set1.issuperset(set2)

# Disjoint disyuncion
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
es_disjoint = set1.isdisjoint(set2)

# frozenset es un set inmutable y mejora la eficiencia en memoria

frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)
