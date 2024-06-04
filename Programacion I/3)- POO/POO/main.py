from class_personaje import *

# def mostrar(heroe: Personaje):
#     print(f"{heroe.nombre} - {heroe.super_poder} - {heroe.poder_pelea}")

personaje_1 = Personaje("Ironman", True, True, "Disparo ultrasonico", 1000)
personaje_2 = Personaje("Antman", True, False, "Convertirse a hormiga", 700)

print(personaje_1.presentarse())
print(personaje_2.presentarse())

personaje_1.volar(500, 250)
personaje_2.volar(300, 80)

personaje_1.atacar(personaje_2)

print(personaje_1.poder_pelea)
print(personaje_2.poder_pelea)
