matriz = [
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]  # Matriz de 3x3


M = len(matriz)  # Numero de filas de la matriz
N = len(matriz[0])  # Numero de columnas de la matriz

# Inicializamos la matriz resultado con ceros
matriz_resultado = [[0]*N for i in range(M)]

escalar = 5  # Escalar por el que multiplicaremos la matriz

for i in range(M):  # FILAS
    for j in range(N):  # COLUMNAS
        # Multiplicamos la matriz por el escalar y lo guardamos en la matriz resultado
        matriz_resultado[i][j] = matriz[i][j] * escalar

for i in range(M):  # FILAS
    for j in range(N):  # COLUMNAS
        # Imprimimos la matriz resultado
        print(f"{matriz_resultado[i][j]:<5}", end=" ")
    print("")
