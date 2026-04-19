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
    # cube
    (1, 1, 0),
    (1, -1, 0),
    (-1, -1, 0),
    (-1, 1, 0),
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]
edge = [
        #cube
        #back
        (0,1),(1,2),(2,3),(3,0),
        #front
        (4,5),(5,6),(6,7),(7,4),
        #sides
        (0,4),(1,5),(2,6),(3,7)
 ]
# fonctions


def line():
    for start, end in edge:
        x = var[start]
        y = var[end]
        h.goto(project(*x))
        h.pendown()
        h.goto(project(*y))
        h.penup()


def project(x, y, z):
    k = (190 * x) / (abs(z) + 1)
    l = (190 * y) / (abs(z) + 1)
    return k, l


def translate_z(x, y, z):

    h.clear()


def frame():
    global dz
    dz += 1 * dt
    translate_z()

    s.ontimer(frame, int(1000/FPS))
    s.update()


line()
s.update()
# s.ontimer(frame, int(1000/FPS))
turtle.exitonclick()
