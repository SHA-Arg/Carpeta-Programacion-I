matriz = [[0]*3 for _ in range(4)]  # Matriz de 4x3


for i in range(len(matriz)):  # FILAS 4
    for j in range(len(matriz[i])):  # COLUMNAS 3
        print(f"{matriz[i][j]}", end=" ")  # Imprime la matriz
    print("")  # Imprime un salto de linea
