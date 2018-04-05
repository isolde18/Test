import turtle
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Josh")

josh=turtle.Turtle()

for c in["yellow","red","purple","blue"]:
    josh.color(c)
    josh.left(90)
    josh.forward(50)
    josh.left(90)
    josh.forward(50)
    josh.left(90)
    josh.forward(50)
    
    
    

wn.mainloop()
