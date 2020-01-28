import turtle
for steps in ['red','blue','green','black']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)
    for microsteps in range(4):
        turtle.forward(50)
        turtle.right(90)       
turtle.done()
