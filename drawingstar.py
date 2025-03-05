import turtle
sc = turtle.Screen()
turtle.Screen().bgcolor("blue")
sc.setup(300,500)
turtle.title("This is the turtle canvas!")
pen = turtle.Turtle()
pen.forward(100)

pen.left(120)
pen.forward(100)

pen.left(120)
pen.forward(100)

pen.penup()
pen.right(150)
pen.forward(70)

pen.pendown()
pen.right(90)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.forward(100)

turtle.done()
