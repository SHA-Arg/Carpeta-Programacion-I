# Explicacion de las variables locales y globales en Python

# En Python, existen dos tipos de variables: variables locales y variables globales. Las variables locales son aquellas que se definen dentro de una funcion y solo pueden ser accedidas desde esa funcion. Por otro lado, las variables globales son aquellas que se definen fuera de una funcion y pueden ser accedidas desde cualquier parte del codigo.

# Por ejemplo:

variable_global = 10


def funcion():
    variable_local = 5
    print(variable_local)
    print(variable_global)


funcion()
print(variable_global)
