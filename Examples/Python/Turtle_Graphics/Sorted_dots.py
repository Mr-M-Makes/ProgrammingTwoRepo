from random import choice, randint, random, randrange
from turtle import Turtle, Screen



def main():
    t: Turtle = Turtle()
    s: Screen = Screen()

    t.penup()
    t.speed(0)
    
    s.colormode(255)
    s.bgcolor("black")

    for dot in range(5000):
        x: int = randint(-400,400)
        y: int = randint(-320,320)

        t.goto(x, y)
        x = abs(x)//2
        y = abs(y)//2
        t.dot(randint(1,50), (x,y,150))
    Screen().exitonclick()


if __name__ == "__main__":
    main()

