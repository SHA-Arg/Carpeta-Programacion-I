# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from Funciones_1 import solicitar_entero


def calcular_potencia(base, exponente):
    potencia = base ** exponente
    return potencia


# -----------------------------------------------
print("Ingrese un numero para la base y un numero para el exponente para calcular la potencia. \n")
print(">> Para la base. \n")
base = solicitar_entero()
print("\n>> Y el exponente. \n")
exponente = solicitar_entero()
potencia = calcular_potencia(base, exponente)
print(f"\n<#> La potencia es: {potencia} \n")

# -----------------------------------------------
