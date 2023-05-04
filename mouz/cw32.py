import turtle

john = turtle.Turtle()

# for i in range(4):
#     john.forward(100)
#     john.right(90)

# for i in range(3):
#     john.forward(150)
#     john.right(120)


def draw_poly(sides : int):
    for _ in range(sides):
        john.forward(120)
        john.right(360 / sides)

turtle.bgcolor("red")

draw_poly(5)


turtle.clear()
# Create a program to draw a filled pink Nonagon using a loop with a background color of green
turtle.bgcolor("green")
john.fillcolor("pink")
john.begin_fill()
draw_poly(9)
john.end_fill()

john.setheading(270)
john.home()

john.penup()
john.setx(-150)
john.sety(150)
john.pendown()

for i in range(5):   
    john.forward(120)
    john.right(144)

john.penup()
john.setx(150)
john.sety(150)
john.pendown()

for i in range(50):
    john.forward(i * 5)
    john.right(144)


turtle.mainloop()


