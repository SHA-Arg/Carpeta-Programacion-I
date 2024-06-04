# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


from Funciones_1 import solicitar_entero


def maximo_de_tres_numeros(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    else:
        return numero3


# --------------------------------------------------------------------------------
# Prueba de la funcion 7|
print("Ingrese tres numeros para encontrar el mayor. \n")
numero1 = solicitar_entero()
print("\n>> Ahora el segundo! ")
numero2 = solicitar_entero()
print("\n>> Y el tercero!")
numero3 = solicitar_entero()
maximo_numero = maximo_de_tres_numeros(numero1, numero2, numero3)
print(f"\n<#> El número más grande es: {maximo_numero} \n")
print("--------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------
