acumulador = 0
for i in range(5):
    numero = input("Ingrese un numero:")
    numero = int(numero)
    acumulador += numero
    # Otra forma de hacerlo
    # acumulador = acumulador + numero

promedio = acumulador / (i+1)

print(f"El promedio es:{promedio} y la suma es:{acumulador}")

# otras formas de hacer el print
# print ("El promedio es:",promedio,"y la suma es:",acumulador)
# print ("El promedio es:"+str(promedio)+" y la suma es:"+str(acumulador))
# print("El promedio es:{} y la suma es:{}".format(promedio, acumulador))
