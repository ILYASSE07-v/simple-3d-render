import turtle
import math

# variables
FPS = 60
dt = 1/FPS
dd = 0
do = 0


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
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, 1, -1),
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]
tempvar = []
edge = [
    # cube
    # back
    (0, 1), (1, 2), (2, 3), (3, 0),
    # front
    (4, 5), (5, 6), (6, 7), (7, 4),
    # sides
    (0, 4), (1, 5), (2, 6), (3, 7)
]
# fonctions


def line():
    for start, end in edge:
        x = tempvar[start]
        y = tempvar[end]
        h.goto(project(*x))
        h.pendown()
        h.goto(project(*y))
        h.penup()


def project(x, y, z):
    factor = 300/(z + 5)
    k = x * factor
    l = y * factor
    return k, l


def rotate(o, p, n):
    c = math.cos(do)
    s = math.sin(do)
    h.clear()
    tempvar.clear()
    for x, y, z in var:
        if o:
            yn = y * c - z * s
            zn = y * s + z * c
            y, z = yn, zn
        if p:
            xn = x * c + z * s
            zn = -x * s + z * c
            x, z = xn, zn
        if n:
            xn = x * c - y * s
            yn = x * s + y * c
            x, y = xn, yn
        tempvar.append((x, y, z))


def translate(o, p, n):
    h.clear()
    tempvar.clear()
    for x, y, z in var:
        if o == True:
            x += dd
        if p == True:
            y += dd
        if n == True:
            z += dd
        tempvar.append((x, y, z))


def frame():
    global dd, do
    p = 1
    if p == True:
        do += 2 * math.pi * dt
        dd += 1 * dt
    else:
        do -= 2 * math.pi * dt
        dd -= 1 * dt
    h.clear()
    rotate(1, 1, 1)
    line()
    s.ontimer(frame, int(1000/FPS))
    s.update()


s.ontimer(frame, int(1000/FPS))
turtle.exitonclick()
