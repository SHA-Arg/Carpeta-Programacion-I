def determinar_numero_par(numero_ingresado):
    if numero_ingresado % 2 == 0:
        mensaje = "El resultado es par"
    else:
        mensaje = "El resultado es impar"
    return mensaje


parametro = input("Ingrese un numero")
parametro = int(parametro)
resultado = determinar_numero_par(parametro)
parametro = str(parametro)

print(f"{resultado, parametro}")
print(type(parametro))
