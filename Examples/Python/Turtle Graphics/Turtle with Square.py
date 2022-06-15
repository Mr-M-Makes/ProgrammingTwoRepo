import turtle

t = turtle.Turtle()
s = turtle.Screen()
x = 0
t.color("cyan")
t.begin_fill()
while x < 4:

    t.forward(150)
    t.right(90)
    x += 1
t.end_fill()
s.bgcolor("black")

turtle.Screen().exitonclick() 