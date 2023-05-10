import turtle as t

t.tracer(False)
def koch(t, order, size):
    if order == 0: # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3) # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

def snow_flake(level : int, size : int):
    for i in range(3):

        t.pencolor(["red", "green", "blue"][i])
        koch(t, level, size)
        t.right(120)


t.pensize(2)

for i in range(3, -1, -1):
    size = 70 * ((i ** 1.5) + 1)
    level = i
    t.penup()
    t.home()
    t.goto(size / -2, size / 3 )
    t.pendown()
    snow_flake(level, size)
    t.penup()

t.home()
t.update()
t.mainloop()