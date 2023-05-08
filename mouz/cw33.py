import turtle

tess = turtle.Turtle()
tess.pensize(2)
turtle.tracer(False)

# All 
tess.setx(-200)
tess.sety(400)
size = 40
for i in range(0, 5):

    for i in range(25):
        # Each quadrant
        for i in range(20):
            # Each row
            tess.pendown()  
            tess.pencolor(0.2, 0.55, 0.55)
            
            for i in range(4):
                tess.forward(size)
                tess.right(90)
            for i in range(3):
                tess.forward(size)
                tess.right(120)
            tess.forward(size)
        tess.right(90)
        tess.forward(size)
        tess.right(90)
        tess.forward(size * 20)
        tess.left(180)
    # tess.home()
    tess.right(90 * i)

turtle.update()

turtle.mainloop()