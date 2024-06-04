# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    else:
        # Obtiene el último dígito del número utilizando el operador módulo ( % ).
        digito_final = numero % 10
        # Divide el número entre 10 (descartando cualquier residuo) para obtener el número restante sin el último dígito.
        digito_anterior = numero // 10
        return digito_final + sumar_digitos(digito_anterior)


numero = 22
resultado = sumar_digitos(numero)
print(resultado)
