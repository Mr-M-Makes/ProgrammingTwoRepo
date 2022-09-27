import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.colormode(255)

r=168
g=50
b=155

t.color((r,g,b))
sides = int(s.numinput("sides","How many sides does your shape have?"))

count = 0

angle = 360/sides
distance = 300/(sides/2)
while count < (sides):
    t.forward(distance)
    t.right(angle)
    count = count + 1


turtle.Screen().exitonclick() 