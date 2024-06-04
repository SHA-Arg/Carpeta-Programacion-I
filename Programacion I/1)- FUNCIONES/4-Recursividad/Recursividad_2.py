# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)


base = 4
exponente = 2

resultado_potencia = calcular_potencia(base, exponente)
print(resultado_potencia)
