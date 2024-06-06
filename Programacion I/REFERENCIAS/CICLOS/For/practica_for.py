import turtle

# Dibujar una ventana
ventana = turtle.Screen()
ventana.bgcolor('black')

# Dibujar la tortuga
tortuga = turtle.Turtle()
tortuga.shape('turtle')
tortuga.color('green')
tortuga.speed(3)

# Dibuja un cuadrado
# for _ in range(4):
#     tortuga.forward(100)
#     tortuga.right(90)
# ventana.exitonclick()

# Dibujar una estrella
for _ in range(5):
    tortuga.forward(250)
    tortuga.right(144)
ventana.exitonclick()

# Dibujar un circulo
# for _ in range(360):
#     tortuga.forward(1)
#     tortuga.right(1)
# ventana.exitonclick()
