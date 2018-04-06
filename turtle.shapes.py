import turtle
wn=turtle.Screen()
tess=turtle.Turtle()
wn.bgcolor("blue")
tess.shape("turtle")
tess.color("pink")
for i in range(4):
    tess.forward(100)
    tess.left(90)

for x in range(3):
    tess.forward(80)
    tess.left(120)

for c in range(30):
    size=20
    
    tess.forward(size)
    tess.left(24)
