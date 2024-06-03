'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''

# Función que ordena un arreglo de números utilizando el algoritmo Bubble Sort


def bubble_sort(array):
    # Recorremos el arreglo
    n = len(array)
    # Recorremos el arreglo n veces
    # En cada iteración, el elemento más grande se coloca al final
    # Por lo tanto, en la primera iteración, el elemento más grande se coloca en la última posición
    for i in range(n-1):
        # Recorremos el arreglo desde el primer elemento hasta el penúltimo
        # En cada iteración, comparamos el elemento actual con el siguiente
        for j in range(n-1-i):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            # De esta forma, el elemento más grande se va moviendo hacia la última posición
            if array[j] > array[j+1]:
                # Intercambiamos los elementos
                array[j], array[j+1] = array[j+1], array[j]


# Ejemplo de uso:
array = [64, 34, 25, 12, 22, 11, 90]
print("Sin ordenarlo:")
print(array)
bubble_sort(array)
print("Arreglo ordenado:")
print(array)
