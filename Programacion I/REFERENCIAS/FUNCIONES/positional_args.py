# Explicacion de los argumentos posicionales en Python
# En Python, existen dos tipos de argumentos que podemos pasar a una funcion: argumentos posicionales y argumentos de palabra clave.
#
# Los argumentos posicionales son aquellos que se pasan a la funcion en el orden en el que fueron definidos. Por ejemplo:
#
# def suma(a, b):
#     return a + b
#
# resultado = suma(2, 3)
# En este caso, los argumentos 2 y 3 son argumentos posicionales, ya que se pasan a la funcion en el orden en el que fueron definidos.
#
# Los argumentos de palabra clave, por otro lado, son aquellos que se pasan a la funcion con su nombre correspondiente. Por ejemplo:
#
# def resta(a, b):
#     return a - b
#
# resultado = resta(a=5, b=3)
# En este caso, los argumentos a y b son argumentos de palabra clave, ya que se pasan a la funcion con su nombre correspondiente.
#
# Los argumentos posicionales son los mas comunes en Python, y su uso es bastante sencillo. Sin embargo, es importante tener en cuenta que si una funcion tiene muchos argumentos posicionales, puede ser dificil recordar el orden en el que deben pasarse.
#
# Para evitar este problema, Python nos permite utilizar argumentos de palabra clave, que nos permiten pasar los argumentos a la funcion con su nombre correspondiente. Esto hace que el codigo sea mas legible y facil de entender.
#
# En resumen, los argumentos posicionales son aquellos que se pasan a la funcion en el orden en el que fueron definidos, mientras que los argumentos de palabra clave son aquellos que se pasan a la funcion con su nombre correspondiente. Ambos tipos de argumentos son utiles en diferentes situaciones, y es importante conocer la diferencia entre ellos para poder utilizarlos de manera efectiva.

def imprimir_nombre(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    print(f"Nombre completo: {primer_nombre} {segundo_nombre} {
          primer_apellido} {segundo_apellido}")


# Posicionales
imprimir_nombre("Juan", "Carlos", "Perez", "Gomez")
# Output: Nombre completo: Juan Carlos Perez Gomez

# Palabra clave
imprimir_nombre(primer_nombre="Juan", segundo_nombre="Carlos",
                primer_apellido="Perez", segundo_apellido="Gomez")
# Output: Nombre completo: Juan Carlos Perez Gomez


# Mezcla de argumentos posicionales y de palabra clave
imprimir_nombre("Juan", "Carlos", primer_apellido="Perez",
                segundo_apellido="Gomez")

# Iterable unpacking (desempaquetado de iterables)
nombres = ["Juan", "Carlos"]
apellidos = ["Perez", "Gomez"]
# Se desempaqueta la lista de nombres y la lista de apellidos en la funcion imprimir_nombre con el operador *
imprimir_nombre(*nombres, *apellidos)
# Output: Nombre completo: Juan Carlos Perez Gomez

# Dictionary unpacking (desempaquetado de diccionarios)
datos = {"primer_nombre": "Juan", "segundo_nombre": "Carlos",
         "primer_apellido": "Perez", "segundo_apellido": "Gomez"}
# Se desempaqueta el diccionario en la funcion imprimir_nombre con el operador **
imprimir_nombre(**datos)
# Output: Nombre completo: Juan Carlos Perez Gomez
