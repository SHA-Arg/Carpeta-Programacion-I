# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from os import system
from Package_Arrays.array_generales import *
from Package_Arrays.especificas import *


def menu_principal():
    numeros = [[0] * 10]
    ingresados = False
    continuar = True

    while (continuar == True):
        print("\nMENU DE OPCIONES:")
        print("\na. Ingresar números")
        print("\nb. Mostrar cantidad de números positivos y negativos")
        print("\nc. Mostrar sumatoria de los números pares")
        print("\nd. Informar el mayor de los números impares")
        print("\ne. Listar todos los números ingresados")
        print("\nf. Listar todos los números pares")
        print("\ng. Listar los números de las posiciones impares")
        print("\nh. Salir")

        opcion = input("Ingrese una opción (a - h): ").strip().lower()

        match opcion:
            case "a":
                if not ingresados:
                    ingreso_numeros(numeros)
                    ingresados = True
                else:
                    print("Ya ingresaste los números.")
            case "b":
                if ingresados:
                    positivos, negativos = contar_positivos_y_negativos(
                        numeros)
                    print(f"Cantidad de números positivos: {positivos}")
                    print(f"Cantidad de números negativos: {negativos}")
                else:
                    print("Primero debes ingresar los números.")
            case "c":
                if ingresados:
                    suma = sumatoria_de_pares(numeros)
                    print(f"La sumatoria de los números pares es: {suma}")
                else:
                    print("Primero debes ingresar los números.")
            case "d":
                if ingresados:
                    mayor = mayor_numero_impar(numeros)
                    print(f"El mayor de los números impares es: {mayor}")
                else:
                    print("Primero debes ingresar los números.")
            case "e":
                if ingresados:
                    print("Números ingresados:")
                    listar_numeros(numeros)
                else:
                    print("Primero debes ingresar los números.")
            case "f":
                if ingresados:
                    print("Números pares:")
                    listar_numeros_pares(numeros)
                else:
                    print("Primero debes ingresar los números.")
            case "g":
                if ingresados:
                    print("Números de posiciones impares:")
                    listar_numeros_impares(numeros)
                else:
                    print("Primero debes ingresar los números.")
            case "h":
                print("¡Hasta luego!")

                break
            case _:
                print("Opción inválida. Intente nuevamente.")

        continuar = input("¿Desea continuar? (s/n): ").strip().lower() == "s"
        if continuar == True:
            continue
        else:
            print("¡Hasta luego!")


if __name__ == "__main__":
    menu_principal()
