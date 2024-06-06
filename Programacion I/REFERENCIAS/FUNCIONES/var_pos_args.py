# Explicacion y ejemplos de parametros posicionales variables en Python

# En Python, es posible definir funciones con un numero variable de parametros posicionales utilizando el operador * en la definicion de la funcion. Estos parametros se conocen como parametros posicionales variables y permiten a una funcion recibir un numero variable de argumentos posicionales.

# Por ejemplo:

def sumar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

    # Otra forma de hacerlo es con la funcion sum de Python
    # resultado = sum(args)
    # return resultado


# En este caso, la funcion sumar recibe un numero variable de argumentos posicionales y devuelve la suma de todos los numeros. Cuando se llama a la funcion, se pueden pasar uno o mas numeros como argumentos, y la funcion los sumara todos.

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)
# Output: 15

resultado = sumar(10, 20, 30)
print(resultado)
# Output: 60

# Los parametros posicionales variables se representan con el operador * seguido de un nombre de variable (en este caso, numeros). Cuando se llama a la funcion, se pueden pasar uno o mas argumentos posicionales, que se recopilan en una tupla dentro de la funcion.

# Los parametros posicionales variables son utiles cuando queremos definir funciones que pueden recibir un numero variable de argumentos posicionales. Esto nos permite crear funciones mas flexibles y generales, que pueden manejar diferentes cantidades de datos de entrada.
