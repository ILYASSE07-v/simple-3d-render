import turtle
import time
import math

# variables
FPS = 60
dt = 1/FPS
dz = 0
doy = 0

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
    k = (200 * x) / z 
    l = (200 * y) / z 
    return k, l


def roate_y():
    h.clear()
    tempvar.clear()
    for x, y, z in var:
        s = math.sin(doy)
        c = math.cos(doy)
        x = x*c - z*s
        z = x*c + z*s
        y = y
        tempvar.append((x, y, z))


def translate_z():
    h.clear()
    tempvar.clear()
    for x, y, z in var:
        x = x
        y = y
        z += dz
        tempvar.append((x, y, z))


def frame():
    global dz
    global doy
    doy = 2 * math.pi * dt
    dz += 1 * dt
    # translate_z()
    roate_y()
    line()
    s.ontimer(frame, int(1000/FPS))
    s.update()


s.ontimer(frame, int(1000/FPS))
turtle.exitonclick()
