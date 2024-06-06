# Explica el uso de *args y **kwargs en funciones.
# Ejemplo:

def calcular_precio_total(*args, **kwargs):
    precio_total = sum(args)
    descuento = kwargs.get('descuento', 0)
    impuestos = kwargs.get('impuestos', 0)

    precio_total -= precio_total * descuento
    precio_total += precio_total * impuestos

    return precio_total


precio = calcular_precio_total(100, 200, 300, descuento=0.1, impuestos=0.16)

# Este ejemplo muestra una funcion llamada calcular_precio_total que acepta un numero variable de argumentos posicionales (*args) y un numero variable de argumentos de palabra clave (**kwargs). Los argumentos posicionales se suman para obtener el precio total, mientras que los argumentos de palabra clave se utilizan para aplicar un descuento y agregar impuestos al precio total. En este caso, se pasan los argumentos 100, 200 y 300 como argumentos posicionales, y se especifica un descuento del 10% y un impuesto del 16% como argumentos de palabra clave. El resultado final es el precio total calculado con el descuento y los impuestos aplicados.
#
# En resumen, *args se utiliza para pasar un numero variable de argumentos posicionales a una funcion, mientras que **kwargs se utiliza para pasar un numero variable de argumentos de palabra clave a una funcion. Esto hace que las funciones sean mas flexibles y puedan aceptar diferentes combinaciones de argumentos sin tener que definir explicitamente todos los parametros.
