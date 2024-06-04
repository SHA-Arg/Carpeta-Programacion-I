# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from os import system
from Package_Modules.Funciones import *

matriz_recaudacion = []


bandera_ingreso = True
while bandera_ingreso:
    print("Bienvenido al sistema de recaudación de colectivos")
    opcion = int(input("""1-Cargar planilla.\n2-Mostrar la recaudación de todos los coches y lineas.\n3-Calcular y mostrar la recaudación por coche\n4-Calcular y mostrar la recaudación total.\n5-Salir\nElija una opcion: """))

    match opcion:
        case 1:
            legajo = int(input("Ingrese legajo del chofer: "))
            if validar_legajo(legajo, legajos):
                linea = int(input("Ingrese línea: "))
                coche = int(input("Ingrese coche: "))
                recaudacion = float(input("Ingrese recaudación: "))
                cargar_planilla(matriz_recaudacion, legajo,
                                linea, coche, recaudacion)
            else:
                print("El legajo ingresado no es válido.")
        case 2:
            print("Recaudación de todos los coches y líneas")
            for recaudacion in matriz_recaudacion:
                print(f"Legajo: {recaudacion[0]} - Línea: {recaudacion[1]} - Coche: {
                      recaudacion[2]} - Recaudación: {recaudacion[3]}")
        case 3:
            # Recaudación por coche
            recaudacion_por_coche = []
            for recaudacion in matriz_recaudacion:
                coche = recaudacion[2]
                if coche not in recaudacion_por_coche:
                    recaudacion_por_coche[coche] = 0
                recaudacion_por_coche[coche] += recaudacion[3]

            for coche, recaudacion in recaudacion_por_coche[coche]:
                print(f"Coche {coche}: ${recaudacion}")
        case 4:
            print("Recaudación total")
        case 5:
            print("Saliendo del programa..")
            break
        case _:
            print("Opción inválida")
    bandera_ingreso = input("Desea seguir ingresando datos? (s/n): ") == "s"

system("pause")
system("cls")
