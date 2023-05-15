import tkinter
import turtle 
import random

john = turtle.Turtle()

def draw_poly(sides : int):
    for _ in range(sides):
        john.forward(120)
        john.right(360 / sides)
    # turtle.mainloop()

def randomshapes():
    while True:
        john.penup()
        john.setx(random.randint(-300, 300))
        john.sety(random.randint(-300, 300))
        john.setheading(random.randint(1, 360))
        john.pendown()
        john.begin_fill()
        pencolor = random.choice(["green", "red", "blue", "orange", "black", "brown", "pink", "purple"])
        fillcolor = random.choice(["green", "red", "blue", "orange", "black", "brown", "pink", "purple"])
        john.color(pencolor, fillcolor)
        sides = random.randint(3, 10)
        draw_poly(sides)
        john.end_fill()

tk = tkinter.Tk()
btn = tkinter.Button(tk, text="click me", command= randomshapes)
btn.pack()
tkinter.mainloop()
