import turtle

myTurtle = turtle.Turtle()
muWin = turtle.Screen()

def draw(myTurtle, length):
    if length  > 0:
        myTurtle.forward(length)
        myTurtle.left(90) #angulo de 90
        draw(myTurtle, length-10)

draw(myTurtle, 100)
myWin.exitonclick()    