#draw 4 circles in the middle of the screen
import turtle
turtle.pensize(5)
turtle.color("black")

def drawCircle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(45)

drawCircle(-25,0)
drawCircle(65,0)
drawCircle(-25,-90)
drawCircle(65,-90)

turtle.done()



