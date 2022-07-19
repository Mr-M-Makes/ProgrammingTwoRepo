from random import choice, randint, random, randrange
from turtle import Turtle, Screen

def rndmclr():
    r = randrange(255)
    g = randrange(255)
    b = randrange(255)

    return (r, g, b)

def main():
    t: Turtle = Turtle()
    s: Screen = Screen()

    t.penup()
    t.speed(0)
    
    s.colormode(255)
    s.bgcolor("black")

    for dot in range(1000):
        x: int = randint(-400,400)
        y: int = randint(-320,320)

        t.goto(x, y)
        t.dot(randint(1,100), rndmclr())


if __name__ == "__main__":
    main()

turtle.Screen().exitonclick()