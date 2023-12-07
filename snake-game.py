import turtle
import time
import random
import imghdr

posponer = 0.1

# Ventana
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza serpiente
cabeza = turtle.Turtle()
turtle.register_shape("./imagen.png")  # Reemplaza "imagen.png" con la ruta correcta de tu archivo de imagen
cabeza.shape("./imagen.png")
cabeza.color("dark green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("turtle")
comida.color("pink")
comida.penup()
comida.goto(0, 100)

# Cuerpo Serpiente
segmento = []

# Marcador
score = 0
high_score = 0

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# Funciones
def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def izquierda():
    cabeza.direction = "left"


def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    # Colisiones bordes
    if (
        cabeza.xcor() > 280
        or cabeza.xcor() < -280
        or cabeza.ycor() > 280
        or cabeza.ycor() < -280
    ):
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        # Esconder los segmentos
        for seg in segmento:
            seg.goto(1000, 1000)

        # Limpiar segmentos lista
        segmento.clear()
        
        score = 0
        texto.clear()
        texto.write(
            "Score: {} High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Colision Comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("light green")
        nuevo_segmento.penup()
        segmento.append(nuevo_segmento)

        # Aumentar marcador
        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write(
            "Score: {} High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Mover el cuerpo
    totalSeg = len(segmento)
    for index in range(totalSeg - 1, 0, -1):
        x = segmento[index - 1].xcor()
        y = segmento[index - 1].ycor()
        segmento[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmento[0].goto(x, y)

    mov()

    # colisiones con el cuerpo
    for seg in segmento:
        if seg.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"
            for seg in segmento:
                seg.goto(1000, 1000)
            # Limpiar segmentos lista
            segmento.clear()
            score = 0
            texto.clear()
            texto.write(
                "Score: {} High Score: {}".format(score, high_score),
                align="center",
                font=("Courier", 24, "normal"),
            )

    time.sleep(posponer)
