import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Zeus & Levs")

zeus = turtle.Turtle()
zeus.color("hotpink")
zeus.pensize(5)

levs = turtle.Turtle()

zeus.forward(80)
zeus.left(120)
zeus.forward(80)
zeus.left(120)
zeus.forward(80)
zeus.left(120)

zeus.right(180)
zeus.forward(80)

levs.forward(50)
levs.left(90)
levs.forward(50)
levs.left(90)
levs.forward(50)
levs.left(90)
levs.forward(50)
levs.left(90)

wn.mainloop()
