import turtle
f=turtle.Turtle()
f.speed(15)
f.color('cyan')
turtle.bgcolor('black')
b=200
while (b>0) :
    f.left(b)
    f.forward(b*2)
    b = b-2
