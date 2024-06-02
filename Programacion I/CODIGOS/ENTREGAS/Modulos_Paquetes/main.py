'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------

EJERCICIO:
Modulos Y Paquetes
1| Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:
PROTOTIPO:
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    pass

En donde:
mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
mínimo: valor mínimo admitido (inclusive)
máximo: valor máximo admitido (inclusive)
reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
En caso de que la función no haya podido conseguir un número válido, la misma retorna None.

1bis| Repetir el mismo procedimiento para un dato de tipo float.

2| Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):
PROTOTIPO:
def get_string(longitud: int) -> str|None:
    pass

Nota: utilizar la función len.

3| Realizar un paquete denominado Package_Input, el mismo deberá contener los siguientes módulos:
Input.py
get_int()
get_float()
get_string()
Validate.py
validate_number()
validate_length()
Nota: estas funciones las tendrán que desarrollar en el módulo Validate y utilizar en el módulo Input.py para realizar las validaciones necesarias.

'''
from Package_Input.validate import *
from Package_Input.input import *

flotante = get_float("Ingrese un numero flotante: ",
                     "Error, ingrese un numero valido: ", 0, 100, 3, "float")

entero = get_int("Ingrese un numero entero: ",
                 "Error, ingrese un numero valido: ", 0, 100, 3, "int")

cadena = get_string("Ingrese una cadena: ",
                    "Error, ingrese una cadena valida: ", 10, 3)

print(f"\nEl numero flotante ingresado es: {flotante}\n El numero entero ingresado es: {
      entero}\n La cadena ingresada es: {cadena}")
