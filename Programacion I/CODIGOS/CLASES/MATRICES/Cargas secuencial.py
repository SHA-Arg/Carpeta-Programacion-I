matriz = [[0]*3 for _ in range(4)]  # Matriz de 4x3


for i in range(len(matriz)):  # FILAS 4
    for j in range(len(matriz[i])):  # COLUMNAS 3
        matriz[i][j] = int(input(f"Ingrese numero: "))  # Carga secuencial
        # Carga secuencial con mensaje personalizado.
        matriz[i][j] = int(
            input(f"Ingrese el valor de la fila {i+1} y columna {j+1}: "))


for i in range(len(matriz)):  # FILAS
    for j in range(len(matriz[i])):  # COLUMNAS
        print(f"{matriz[i][j]}", end=" ")  # Imprime la matriz
    print("")  # Imprime un salto de linea
