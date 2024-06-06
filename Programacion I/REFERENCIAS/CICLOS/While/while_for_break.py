import random
import turtle


# Solo pueden avanzar si el numero ramdom es impar

condicion_salida = 'continuar'

while condicion_salida == 'continuar':
    # limpiar pantalla
    ventana = turtle.resetscreen()

    # Pantalla del juego
    ventana = turtle.Screen()
    ventana.title("Carrera de Tortugas")
    ventana.bgcolor("black")
    ventana.setup(width=800, height=600)

    meta = 300

    # Tortuga Jugador 1
    tortuga_1 = turtle.Turtle()
    tortuga_1.shape("turtle")
    tortuga_1.color("red")
    tortuga_1.penup()
    tortuga_1.goto(-200, 100)

    # Tortuga Jugador 2
    tortuga_2 = turtle.Turtle()
    tortuga_2.shape("turtle")
    tortuga_2.color("blue")
    tortuga_2.penup()
    tortuga_2.goto(-200, -100)

    # Linea de Meta
    meta_linea = turtle.Turtle()
    meta_linea.penup()
    meta_linea.goto(meta, 200)
    meta_linea.pendown()
    meta_linea.color("white")
    meta_linea.goto(meta, -150)
    meta_linea.hideturtle()

    # Largada de la carrera
    meta_linea = turtle.Turtle()
    meta_linea.penup()
    meta_linea.goto(meta, 200)
    meta_linea.pendown()
    meta_linea.color("green")
    meta_linea.goto(meta, -150)
    meta_linea.hideturtle()

    while tortuga_1.xcor() < meta and tortuga_2.xcor() < meta:
        avanza_tortuga_1 = random.randint(1, 20)
        avanza_tortuga_2 = random.randint(1, 20)

        if avanza_tortuga_1 % 2 == 0 or avanza_tortuga_2 % 2 == 0:
            continue

        tortuga_1.forward(avanza_tortuga_1)
        tortuga_2.forward(avanza_tortuga_2)

        print(f"Tortuga Roja: {
              avanza_tortuga_1} - Tortuga Azul: {avanza_tortuga_2}")

        if tortuga_1.xcor() >= meta:
            print("Ganó la tortuga Roja!!")
            break
        elif tortuga_2.xcor() >= meta:
            print("Ganó la tortuga Azul!!")
            break
        elif tortuga_1 == tortuga_2:
            print("Ningúna tortuga pudo ganar, es un empate!!")
            break

    condicion_salida = input('Desea continuar? (continuar / salir): ')

    if condicion_salida == 'salir':
        print("Gracias por jugar!!")
        break
    else:
        continue

    ventana.mainloop()
