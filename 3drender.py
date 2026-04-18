import turtle
import time

# variables
FPS = 30
dt = 1/FPS
dz = 0


# setting screen
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=600, height=600)
s.tracer(0)

# header
h = turtle.Turtle()
h.penup()
h.color("green")
h.shape("square")
h.speed(0)

# 3d cordinates
var = [
    (0.5, 0, 1)
    (-0.5, 0, 1)
    (0.5, 0, 2)
    (-0.5, 0, 2)
]

# fonctions


def project(x, y, z):
    k = (190 * x) / z
    l = (190 * y)/z
    return k, l


def frame():
    global dz
    dz += 1 * dt
    h.clear()

    cord = project(0.5, 0, 1 + dz)


s.update()
s.ontimer(frame, int(1000/FPS))

turtle.exitonclick()
