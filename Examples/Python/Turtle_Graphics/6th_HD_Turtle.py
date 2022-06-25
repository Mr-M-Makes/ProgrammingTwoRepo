import turtle
import math

t = turtle.Turtle()
s = turtle.Screen()
s.colormode(255)

x = 0
y=0
angle=90
dist = 300
increment = .97
t.speed(0)
r=250
g=250
b=250

while y < 1000:    
    t.color((r, g, b))
    
    t.begin_fill()
    while x < 4:
        t.forward(dist)
        t.right(angle)
        x += 1
        print(r)
        dist = dist*.99
    t.end_fill()
    
    r = max(math.floor(r*increment-3),0)
    b = max(math.floor(b*increment-5),0)
    g = max(math.floor(g*increment-10),0)
    
    x = 0
    y += 1
    
    dist = dist*increment
turtle.Screen().exitonclick()     