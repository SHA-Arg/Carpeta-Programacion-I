from class_personaje import *
from main import *


def mostrar_lista_personaje(lista: list[Personaje]):
    for heroe in lista_heroes:
        print(heroe.presentarse())


personaje_1 = Personaje("Ironman", True, True, "Disparo ultrasonico", 1000)
personaje_2 = Personaje("Ant-man", True, False, "Convertirse a hormiga", 700)
personaje_3 = Personaje("Thor", False, True, "Trueno", 2000)
personaje_4 = Personaje("Spiderman", True, False, "Golpe aracnido", 850)

lista_heroes = []

lista_heroes.append(personaje_1)
lista_heroes.append(personaje_2)
lista_heroes.append(personaje_3)

mostrar_lista_personaje(lista_heroes)


lista_heroes.insert(1, personaje_4)
mostrar_lista_personaje(lista_heroes)


lista_heroes.remove(personaje_1)
mostrar_lista_personaje(lista_heroes)


lista_heroes.sort()
mostrar_lista_personaje(lista_heroes)
