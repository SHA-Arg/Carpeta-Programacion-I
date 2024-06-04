

from os import system
from Package.class_video import Video
from Package.data import *

bandera_ingreso = False
bandera_seguir = True

while bandera_seguir:
    opcion = (input("""
                    a.Normalizar objetos:\n
                    b.Mostrar temas\n
                    c.Ordenar temas\n
                    d.Promedio de visitas\n
                    e.Maxima reproduccion\n
                    f.Busqueda por codigo\n
                    g.Listar por colaborador \n
                    h.Listar por mes\n
                    i.Salir\n
                    Elija una opcion: """))

    match opcion:
        case "a":
            for i in range(len(lista_videos)):
                lista_videos[i].dividir_titulo()
                lista_videos[i].obtener_codigo_url()
                lista_videos[i].formatear_fecha()

        # case "b":

        # case "c":
        # case "e":

        # case "f":

        # case "g":

        # case "h":

        # case None:


system("pause")
system("cls")
