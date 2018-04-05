import turtle

wn=turtle.Screen()
wn.bgcolor("orange")

clrs= ["yellow","red","purple","blue"]
for c in clrs:
    turtle.color(c)
    turtle.pensize(5)
    turtle.forward(50)
    turtle.left(90)

wn.mainloop()
