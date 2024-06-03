"""
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------

Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:

-Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
-Mostrar la recaudación de todos los coches y líneas.
-Calcular y mostrar recaudación por línea.
-Calcular y mostrar recaudación por coche.
-Calcular y mostrar la recaudación total.
-Salir

Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.

"""


def generar_legajos(filas, columnas):
    inicio = 1000
    legajos = []
    for i in range(filas):
        nueva_fila = []
        for j in range(columnas):
            nueva_fila += [inicio]
            inicio += 1
        legajos += [nueva_fila]
    return legajos


legajos = generar_legajos(3, 5)
for fila in legajos:
    print(fila)


def validar_legajo(legajo, matriz_legajos):
    for fila in matriz_legajos:
        if legajo in fila:
            return True
    return False


def cargar_planilla(matriz_recaudacion, legajo, linea, coche, recaudacion):
    nueva_recaudacion = [legajo, linea, coche, recaudacion]
    matriz_recaudacion += [nueva_recaudacion]


def calcular_recaudacion_por_linea(matriz_recaudacion):
    recaudacion_por_linea = []
    for recaudacion in matriz_recaudacion:
        linea = recaudacion[1]
        if linea != recaudacion_por_linea:
            recaudacion_por_linea[linea] = 0
        recaudacion_por_linea[linea] += recaudacion[3]

    for linea, recaudacion in recaudacion_por_linea[linea]:
        print(f"Línea {linea}: ${recaudacion}")


def calcular_recaudacion_por_coche(matriz_recaudacion):
    recaudacion_por_coche = []
    for recaudacion in matriz_recaudacion:
        coche = recaudacion[2]
        if coche != recaudacion_por_coche:
            recaudacion_por_coche[coche] = 0
        recaudacion_por_coche[coche] += recaudacion[3]

    for coche, recaudacion in recaudacion_por_coche[coche]:
        print(f"Coche {coche}: ${recaudacion}")


def calcular_recaudacion_total(matriz_recaudacion):
    recaudacion_total = 0
    for recaudacion in matriz_recaudacion:
        recaudacion_total += recaudacion[3]
    print(f"Recaudación total: ${recaudacion_total}")
