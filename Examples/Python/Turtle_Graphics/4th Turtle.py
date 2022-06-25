import turtle

t = turtle.Turtle()

s = turtle.Screen()
s.colormode(255)
x = 0
y=0
angle=90
dist = 150
increment = .9
#turtle.fillcolor((r,g,b))
r=20
g=20
b=20
while y < 50:    
    t.color((r, g, b))
    t.begin_fill()
    while x < 4:
        t.forward(dist)
        t.right(angle)
        x += 1
        
        print(r)
    t.end_fill()
    r+=5
    g+=5
    b+=5    
    x = 0
    y += 1
    dist = dist*increment
    
    




turtle.Screen().exitonclick() 