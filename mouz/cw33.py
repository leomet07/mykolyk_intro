import turtle
import math

tess = turtle.Turtle()
tess.pensize(2)
turtle.tracer(False)

def move_turtle(x : float, y : float):
    tess.penup()
    tess.home()
    tess.setx(x)
    tess.sety(y)
    tess.pendown()

def draw_rect(x : float, y : float, w : float, h : float):
    move_turtle(x , y)
    for i in range(4):
        if i % 2 == 0:
            tess.forward(w)
        else:
            tess.forward(h)
        tess.left(90)



def draw_circle(x : float, y : float, radius : float):
    move_turtle(x , y)
    # Forward 1: rad 57.2957795130823208768
    # Forward 2: rad 114.5915590261646417536
    forward = (radius * math.pi * 2) / 360
    for i in range(480):
        tess.forward(forward)
        tess.right(1)
        

def draw_bus(x : float, y : float, size : float):
    w = size * 10
    h = size * 5
    draw_rect(x, y, w, h)
    draw_circle(x + size, y + size, size)
    draw_circle(x + w - size, y + size, size)

# draw_bus()
# draw_circle(-250, -25, 200)
# tess.setheading(0)
# draw_rect(69, 69, 300, 90)
tess.penup()
draw_bus(50, 50, 30)
turtle.update()

turtle.mainloop()