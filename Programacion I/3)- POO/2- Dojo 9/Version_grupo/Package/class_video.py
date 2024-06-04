from datetime import datetime


class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None

    def mostrar_tema(self):
        # Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {
              self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*30)

    def dividir_titulo(self):
        sesion_colaborador = self.titulo.split("|")
        self.colaborador = sesion_colaborador[0]
        self.sesion = sesion_colaborador[1]

    def obtener_codigo_url(self):
        codigo_url = self.url_youtube.split("=")
        self.url_youtube = codigo_url[1]

    def formatear_fecha(self):
        # Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        # Para ello deberán dividir la fecha (en formato string) en dia, mes y año y a partir de
        # esos datos, crear la nueva fecha.
        fecha = self.fecha_lanzamiento.split("-")
        # año = fecha[0]
        # mes = fecha[1]
        # dia = fecha[2]
        # nueva_fecha = datetime(int(fecha[0]),int(fecha[1]),int(fecha[2]))
        nueva_fecha = datetime(int(fecha[0]), int(
            fecha[1]), int(fecha[2])).strftime("%d-%m-%Y")

        return nueva_fecha
