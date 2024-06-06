# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

def sumar_naturales(numero: int) -> int:
    if numero <= 0:
        return 0
    else:
        sumar_naturales(numero)
        return numero + sumar_naturales(numero - 1)


numero_a_sumar = int(input("Ingrese un numero: "))

resultado = sumar_naturales(numero_a_sumar)
print(resultado)
