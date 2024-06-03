lista = [5, 3, 1, 4, 2]

for i in range(0, len(lista) - 1):  # Verde
    for j in range(i+1, len(lista)):  # Naranja
        if lista[i] > lista[j]:  # Criterio de ordenamiento
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar

print(lista)

# a = 8
# b = 5

# c = a
# a = b     #Forma correcta de hacerlo
# b = c

# print(a)
# print(b)
