matriz = [
    [4, 9, 6],
    [7, 9, 3],
    [1, 2, 3],
    [7, 2, 8]
]

for i in range(len(matriz)):  # Filas
    for j in range(len(matriz[i])):  # Columnas
        print(f"{matriz[i][j]}", end=" ")
    print("")
