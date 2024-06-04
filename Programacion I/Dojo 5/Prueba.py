# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


def multiplicar_matrices(matriz1, matriz2):
    # Verificar si las matrices se pueden multiplicar
    if len(matriz1[0]) != len(matriz2):
        print("No se pueden multiplicar las matrices. Las dimensiones no son consistentes.")
        return None
    # Crear una matriz vacía para almacenar el resultado
    resultado = []
    # Recorrer las filas de la primera matriz
    # Para cada fila, recorrer las columnas de la segunda matriz
    for i in range(len(matriz1)):
        # Crear una fila vacía para almacenar los valores de la fila actual
        fila = []
        # Recorrer las columnas de la segunda matriz
        # Para cada columna, calcular el producto punto de la fila actual de la primera matriz
        for j in range(len(matriz2[0])):
            # Inicializar la suma en cero
            suma = 0
            # Calcular el producto punto de la fila actual de la primera matriz con la columna actual de la segunda matriz
            # Recorrer los elementos de la fila actual de la primera matriz y la columna actual de la segunda matriz
            for k in range(len(matriz2)):
                # Sumar el producto de los elementos correspondientes
                # de la fila actual de la primera matriz y la columna actual de la segunda matriz
                suma += matriz1[i][k] * matriz2[k][j]
                # Agregar el resultado a la fila actual
            # Agregar la suma a la fila actual
            # La fila actual contendrá los valores de la fila actual de la primera matriz
            fila += [suma]
            # Agregar la fila actual al resultado
            # El resultado contendrá las filas de la primera matriz multiplicadas por la segunda matriz
        resultado += [fila]
    return resultado

# Función que solicita al usuario ingresar una matriz
# y la devuelve como una lista de listas


def ingresar_matriz():
    # Solicitar al usuario el número de filas y columnas de la matriz
    filas = int(input("Ingrese el número de filas: "))
    # Solicitar al usuario el número de columnas de la matriz
    columnas = int(input("Ingrese el número de columnas: "))
    # Crear una matriz vacía para almacenar los valores
    matriz = []
    # Recorrer las filas de la matriz
    for i in range(filas):
        # Crear una fila vacía para almacenar los valores de la fila actual
        fila = []
        # Recorrer las columnas de la matriz
        # Para cada columna, solicitar al usuario ingresar un valor
        for j in range(columnas):
            valor = int(
                input(f"Ingrese el valor de la posición ({i+1},{j+1}): "))
            fila += [valor]
        matriz += [fila]
    return matriz


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


matriz1 = ingresar_matriz()
matriz2 = ingresar_matriz()

print("\nMatriz 1:")
mostrar_matriz(matriz1)
print("\nMatriz 2:")
mostrar_matriz(matriz2)

resultado = multiplicar_matrices(matriz1, matriz2)
if resultado:
    print("\nResultado de la multiplicación:")
    mostrar_matriz(resultado)
