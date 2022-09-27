import turtle
import random

bob = turtle.Screen()       #create window Object
bobby =turtle.Turtle()      #Contruct turtle object

#set Color mode to (r,g,b)
bob.colormode(255)          

#put the whole program into a loop that we can close on command
Quit = 0
while Quit == 0:

    #Lift pen - move - put down pen AKA move without drawing
    bobby.penup()
    bobby.goto(random.randint(-200,200), random.randint(-200,200))
    bobby.pendown()

    #set random Color
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    bobby.color((r,g,b))

    #Start making regular polygon
    cheese =0
    sides = int(bob.numinput("sides","How many sides does your shape have?")) #ask how many sides
    angle = 360/sides #equation for exterior angle

    distance = 300/(sides/2)    #Scale to fit screen

    #Start Drawing
    bobby.begin_fill()
    while cheese < sides :
        bobby.forward(distance)
        bobby.right(angle)
        cheese += 1
    bobby.end_fill()

    #ask if quitting
    Answer = bob.textinput("Quit?","Type \"QUIT\" to close")

    if Answer == "QUIT":
        Quit = 1 # Set quit to true
        continue #End loop and go to beginning
    else:
        Quit = 0 # Just to be sure that it doesn't quit and nothing accidentally chagned the variable- shouldn't matter
turtle.Screen().exitonclick() # Keep window open