import turtle

t = turtle.Turtle()
s = turtle.Screen()
x = 0
y=0
angle=90
dist = 150
increment = 30
while y < 11:    
    while x < 4:

        t.forward(dist)
        t.right(angle)
        x += 1
        
    x = 0
    y += 1
    dist -= increment
    increment / 10
    
turtle.Screen().exitonclick() 
