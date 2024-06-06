# Explicacion y ejemplos de argumentos opcionales en Python

# Los argumentos opcionales en Python son aquellos que tienen un valor por defecto y pueden ser omitidos al llamar a una funcion. Esto nos permite definir funciones con parametros que no son obligatorios y que tienen un valor por defecto en caso de no ser especificados.

# Por ejemplo:

def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")


saludar("Juan")
# Output: Hola, Juan!

saludar("Maria", "Buenos dias")
# Output: Buenos dias, Maria!

# En este caso, la funcion saludar tiene un argumento opcional llamado saludo que tiene un valor por defecto de "Hola". Cuando se llama a la funcion sin especificar el valor de saludo, se utiliza el valor por defecto. Sin embargo, si se especifica un valor para saludo al llamar a la funcion, se utiliza ese valor en lugar del valor por defecto.

# Los argumentos opcionales son utiles cuando queremos definir funciones con parametros que no son obligatorios y que tienen un valor por defecto en caso de no ser especificados. Esto nos permite tener funciones mas flexibles y faciles de usar, ya que no es necesario especificar todos los parametros al llamar a la funcion.


def calcular_precio(producto, cantidad, precio_u,  descuento=0):
    precio_final = cantidad * precio_u * (1 - descuento)
    print(f"El precio final de {cantidad} unidades de {
          producto} es: {precio_final}")


calcular_precio("manzanas", 5, 2.5)
# Output: El precio final de 5 unidades de manzanas es: 12.5

calcular_precio("manzanas", 5, 2.5, 0.1)
# Output: El precio final de 5 unidades de manzanas es: 11.25


# En resumen, los argumentos opcionales en Python son aquellos que tienen un valor por defecto y pueden ser omitidos al llamar a una funcion. Esto nos permite definir funciones con parametros que no son obligatorios y que tienen un valor por defecto en caso de no ser especificados. Los argumentos opcionales son utiles para hacer que las funciones sean mas flexibles y faciles de usar.
