def insert_sort(matriz):
    for i in range(1, len(matriz)):
        key = matriz[i]
        j = i - 1
        while j >= 0 and key < matriz[j]:
            matriz[j + 1] = matriz[j]
            j -= 1
        matriz[j + 1] = key


def bubble_sort(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(0, n - i - 1):
            if matriz[j] > matriz[j + 1]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]


# matriz = [64, 34, 25, 12, 22, 11, 90]
# print("Array original:", matriz)
# insert_sort(matriz)
# print("Después de Insertion Sort:", matriz)
matriz2 = ["Carlos", "Ana", "Beto", "Diana",
           "Elena", "Fernando", "Gustavo", "Hugo", "Irene"]
print("Array original:", matriz2)
insert_sort(matriz2)
print("Después de Bubble Sort:", matriz2)
