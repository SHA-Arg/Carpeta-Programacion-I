import random

meta = 20

caracol1 = 0
caracol2 = 0

while caracol1 < meta and caracol2 < meta:
    avanza_caracol1 = random.randint(1, 3)
    avanza_caracol2 = random.randint(1, 3)

    caracol1 += avanza_caracol1
    caracol2 += avanza_caracol2

    print(f"Caracol 1 avanza: {avanza_caracol1}, total avanzado: {caracol1}")
    print(f"Caracol 2avanza: {avanza_caracol2}, total avanzado: {caracol2} ")
    print("-------------------")

    # / Version 1
    # if caracol1 >= meta:
    #     print("Ganó el caracol 1")
    #     break
    # elif caracol2 >= meta:
    #     print("Ganó el caracol 2")
    #     break
    # else:
    #     print("Ningún caracol gano, es un empate")

    if caracol1 >= 20 or caracol1 >= 20:
        break

if caracol1 > caracol2:
    print("El Caracol Rojo Gano!")
elif caracol2 > caracol1:
    print("El Caracol Azul Gano!")
else:
    print("Fue Empate!!")
