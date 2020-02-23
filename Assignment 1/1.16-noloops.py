#draw 4 circles in the middle of the screen
import turtle
turtle.pensize(5)
turtle.color("black")

turtle.penup()
turtle.goto(-25,0)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(65,0)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(-25,-90)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(65,-90)
turtle.pendown()
turtle.circle(45)
