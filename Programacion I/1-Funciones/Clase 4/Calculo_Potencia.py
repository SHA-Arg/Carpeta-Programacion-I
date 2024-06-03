def calcular_potencia(numero: int, exponente: int) -> int:
    # busco el caso base.
    if exponente == 0:
        resultado = 1
    else:
        resultado = numero * calcular_potencia(numero, exponente - 1)
    return resultado


base = input("Ingrese la base: ")
base = int(base)
exponente = input("Ingrese el exponente:")
exponente = int(exponente)
calculo = calcular_potencia(base, exponente)
print(calculo)
