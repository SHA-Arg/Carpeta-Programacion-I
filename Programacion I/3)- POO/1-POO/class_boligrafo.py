# clase llamada Bolígrafo.

# Los atributos serán los siguientes:
# capacidad_tinta_maxima
# grosor_punta
# color
# cantidad_tinta
class boligrafo:
    def __init__(self, capacidad_tinta_maxima: int, grosor_punta: int, color: str, cantidad_tinta: int):
        self.capacidad_tinta_maxima = capacidad_tinta_maxima
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantidad_tinta = cantidad_tinta
