matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        # :<5 es para alinear a la izquierda
        print(f"{matriz[i][j]:<5}", end=" ")  # Imprime la matriz transpuesta
    print("")
