import turtle
import time

# variables
FPS = 60
dt = 1/FPS
dz = 0


# setting screen
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=600, height=600)
s.tracer(0)

# header
h = turtle.Turtle()
h.hideturtle()
h.pencolor("green")
h.penup()
h.shape("square")
h.speed(0)

# 3d cordinates
var = [
    (1, 1, 1),
    (1, -1, 1),
    (1, -1, 2),
    (1, 1, 2),
    (-1, 1, 1),
    (-1, -1, 1),
    (-1, -1, 2),
    (-1, 1, 2)
]

# fonctions


def project(x, y, z):
    k = (190 * x) / z
    l = (190 * y)/z
    return k, l


def translate_z():
    h.clear()
    for x, y, z in var:
        h.goto(*project(x, y, z + dz))
        h.pendown()


def frame():
    global dz
    dz += 1 * dt
    translate_z()
    s.ontimer(frame, int(100/FPS))
    s.update()


s.update()
s.ontimer(frame, int(100/FPS))

turtle.exitonclick()
