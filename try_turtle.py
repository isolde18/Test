import turtle

wn=turtle.Screen()
wn.bgcolor("orange")

for c in ["yellow","red","purple","blue"]:
    turtle.color(c)
    turtle.pensize(5)
    turtle.forward(50)
    turtle.left(90)

wn.mainloop()
