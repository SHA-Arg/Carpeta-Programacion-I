'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''


from random import randint


def generar_legajos():
    choferes = 15
    legajos = [0] * choferes

    for i in range(choferes):
        generador = randint(0, 1000)
        legajos[i] = generador
    return legajos


def mostrar_legajos(legajos: list):
    print("Los legajos de los choferes son los siguientes:")
    for i in range(len(legajos)):
        mostrar = legajos[i]
        print(f"{mostrar: 05}", end=" ")
        print()


def comprobar_legajos(legajos: list):
    bandera = True
    mostrar_legajos(legajos)

    while bandera:
        ingreso = int(input("Legajo del chofer: "))
        for i in range(len(legajos)):
            if legajos[i] == ingreso:
                bandera = False
                print("exito")
        if bandera == True:
            print("ERROR, el legajo que ingreso no se encuentra, ingrese nuevamente.")

    return bandera
