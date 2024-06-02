matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

matriz_b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

M = len(matriz_a)  # Numero de filas
N = len(matriz_a[0])  # Numero de columnas

# Inicializamos la matriz resultado con ceros
matriz_resultado = [[0]*N for i in range(M)]

# Sumamos las matrices
for i in range(M):  # Recorremos las filas
    for j in range(N):  # Recorremos las columnas
        # Sumamos los elementos de las matrices
        matriz_resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

# Imprimimos la matriz resultado
for i in range(M):  # Recorremos las filas
    for j in range(N):  # Recorremos las columnas
        # Imprimimos la matriz resultado
        print(f"{matriz_resultado[i][j]:<5}", end=" ")
    print("")
