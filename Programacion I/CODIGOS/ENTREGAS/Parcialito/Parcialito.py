'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
CONSIGNA PARCIALITO:

Desarrollar una función que reciba como parametros el precio de un producto y el porcentaje de descuento que se aplicara. La funcion retornara el precio del producto con descuento.

'''


def calcular_precio_con_descuento(precio_de_un_producto: float, porcentaje_descuento: float) -> float:
    descuento = precio_de_un_producto * (porcentaje_descuento / 100)
    precio_con_descuento = precio_de_un_producto - descuento
    return precio_con_descuento


# Test
print(calcular_precio_con_descuento(100, 10))  # 90.0
print(calcular_precio_con_descuento(100, 20))  # 80.0
