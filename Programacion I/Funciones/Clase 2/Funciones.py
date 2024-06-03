import random

print("--------------------------------------------------")
print(">> Funciones.")
print("--------------------------------------------------")
print(">> Suma sin funcion.")
un_numero = input("Ingrese el primer numero a sumar: ")
un_numero = int(un_numero)
otro_numero = input("Ingrese el segundo numero a sumar: ")
otro_numero = int(otro_numero)

suma = un_numero + otro_numero

print(f"El resultado de la suma es: {suma}")


print("--------------------------------------------------")
print(" >> Suma 1 con print dentro de la funcion.")
print("# Se piden los numeros dentro de la funcion pero No se deberia pedrir los numeros dentro de una funcion.")


def sumar_1():  # Con print dentro de la funcion.
    un_numero = input("Ingrese el primer numero a sumar: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese el segundo numero a sumar: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    print(f"El resultado de la suma es: {suma}")


print(">> Suma 2 con return dentro de la funcion entonces no devuelve nada.")


def sumar_3():  # Con return dentro de la funcion.
    un_numero = input("Ingrese el primer numero a sumar: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese el segundo numero a sumar: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    return suma


print("\n--------------------------------------------------")
print(">> Suma 2 ")
print("# Se piden los numeros fuera de la funcion y se pasan como parametros a la funcion.")


def sumar_2(un_numero, otro_numero):  # Con print dentro de la funcion.
    suma = un_numero + otro_numero

    print(f"El resultado de la suma es: {suma}")


print("--------------------------------------------------")


def sumar_4(un_numero, otro_numero):  # Con return dentro de la funcion.
    suma = un_numero + otro_numero
    return suma


print(f"El resultado de la suma es: {suma}")

print("--------------------------------------------------")

# Instancia de invocacion de una funcion
sumar_2(8, 9)

print("--------------------------------------------------")

# Se le solicita al usuario que ingrese los numeros a sumar.
un_numero = input("Ingrese el primer numero a sumar: ")
un_numero = int(un_numero)
otro_numero = input("Ingrese el segundo numero a sumar: ")
otro_numero = int(otro_numero)
# Instancia de invocacion de una funcion
sumar_2(un_numero, otro_numero)

print("--------------------------------------------------")
# Le paso dos numeros aleatorios
un_numero = random.randint(1, 100)
otro_numero = random.randint(500, 700)
# Instancia de invocacion de una funcion
sumar_2(un_numero, otro_numero)  # Recibe parametros pero NO devuelve nada.

print("--------------------------------------------------")

sumar_3()
resultado = sumar_3()
print(f"El resultado de la suma es : {resultado}")

print("--------------------------------------------------")

# Esta funcion recibe numeros y no le interesa de donde vienen, hace lo que tiene que hacer y retorna lo que tiene que retornar, no le interesa para donde va lo que retorna. Es una funcion independiente y reutilizable.

un_numero = input("Ingrese el primer numero a sumar: ")
un_numero = int(un_numero)
otro_numero = input("Ingrese el segundo numero a sumar: ")
otro_numero = int(otro_numero)

# Recibe parametros y retorna el resultado. Los parametros en este caso ya estan ingresados por otro lado. Obviamente tengo que guardar la suma del resultado en una variable.
resultado = sumar_4(un_numero, otro_numero)

print(resultado)
print("--------------------------------------------------")
