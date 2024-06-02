'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------

Ejercicio 1:
Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ej:
cadena = “murcielaguito”


'''


def cantidad_de_vocales(cadena):
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0

    resultado = [[0]*2 for _ in range(5)]

    for i in range(len(cadena)):
        match cadena[i]:
            case "a":
                cont_a += 1
            case "e":
                cont_e += 1
            case "i":
                cont_i += 1
            case "o":
                cont_o += 1
            case "u":
                cont_u += 1

    resultado[0][0] = "a"
    resultado[0][1] = cont_a
    resultado[1][0] = "e"
    resultado[1][1] = cont_e
    resultado[2][0] = "i"
    resultado[2][1] = cont_i
    resultado[3][0] = "o"
    resultado[3][1] = cont_o
    resultado[4][0] = "u"
    resultado[4][1] = cont_u
    return resultado


cadena = "SebastianAmaralhereñu"
print(cantidad_de_vocales(cadena))
