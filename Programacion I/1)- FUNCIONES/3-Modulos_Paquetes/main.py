# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

from Package_Input.input import get_float, get_int, get_string

flotante = get_float("Ingrese un numero flotante: ",
                     "Error, ingrese un numero valido: ", 0, 100, 3, "float")

entero = get_int("Ingrese un numero entero: ",
                 "Error, ingrese un numero valido: ", 0, 100, 3, "int")

cadena = get_string("Ingrese una cadena: ",
                    "Error, ingrese una cadena valida: ", 10, 3)

print(f"El numero flotante ingresado es: {flotante}\n El numero entero ingresado es: {
      entero} \n La cadena ingresada es: {cadena}")
