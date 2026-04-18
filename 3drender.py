import turtle


def point(x, y):
    h = turtle.Turtle()
    h.penup()
    h.color("green")
    h.shape("square")
    h.goto(x, y)
    return x, y


def screen(x, y):
    k = (x * 580) / 2
    l = (y * 580) / 2
    return k, l


def project(x, y, z):
    k = x/z
    l = y/z
    return k, l

def frame():
    s.tracer(1)
    point(*screen(*project(0, 0, 2)))


# setting screen
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=600, height=600)
s.tracer(0)

# main loop

s.update()
turtle.done()
