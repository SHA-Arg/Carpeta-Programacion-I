"""
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------

Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.

"""

from os import system
from Packages.class_video import *
from Packages.data import *
from datetime import datetime

bandera_ingreso = False
bandera_seguir = True


while bandera_seguir == True:
    opcion = input("Ingrese una opción:\n a) Normalizar objetos\n b) Mostrar temas\n c) Ordenar temas\n d) Promedio de vistas\n e) Máxima reproducción\n f) Búsqueda por código\n g) Listar por colaborador\n h) Listar por mes\n i) Salir:\n ")

    match opcion:
        case "a":
            for video in lista_videos:
                video.dividir_titulo()
                video.obtener_codigo_url()
                video.formatear_fecha()

        # MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
        case "b":
            for video in lista_videos:
                video.mostrar_tema()

        # ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
        case "c":
            lista_ordenada = []
            for video in lista_videos:
                lista_ordenada.append(video)

            for lista in range(len(lista_ordenada)):
                for i in range(len(lista_ordenada)-1):
                    if lista_ordenada[i].sesion > lista_ordenada[i+1].sesion:
                        lista_ordenada[i], lista_ordenada[i +
                                                          1] = lista_ordenada[i+1], lista_ordenada[i]

            for video in lista_ordenada:
                video.mostrar_tema()

        # PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
        case "d":
            suma_vistas = 0
            for video in lista_videos:
                suma_vistas += video.vistas
            promedio_vistas = suma_vistas / len(lista_videos)
            print(f"El promedio de vistas es: {promedio_vistas/1000}k")

        # MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
        case "e":
            max_vistas = 0
            for video in lista_videos:
                if video.vistas > max_vistas:
                    max_vistas = video.vistas
            for video in lista_videos:
                if video.vistas == max_vistas:
                    video.mostrar_tema()

        # MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
        case "f":
            for video in lista_videos:
                if video.url_youtube.startswith("nick"):
                    video.mostrar_tema()

        #  BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
        case "g":
            colaborador = input("Ingrese el nombre del colaborador: ")
            for video in lista_videos:
                if video.colaborador == colaborador:
                    video.mostrar_tema()

        # LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de
        case "h":
            mes = input("Ingrese el mes: ")
            for video in lista_videos:
                if video.fecha_lanzamiento.month == mes:
                    video.mostrar_tema()

        # LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
        case "i":
            bandera_seguir = False
        case _:
            print("Opción inválida")

    system("pause")
    system("cls")
