from my_classes import Shape, Square, Triangle
from turtle import Screen

def main():
    win = Screen()
    win.bgcolor("black")

    s1 = Shape("Bob", "blue", (100, 100), 150)
    print(s1)
    s1.draw()

    s2 = Square("Sal", "yellow", (100, 100), 150)
    print(s2)
    s2.draw()

    s3 = Triangle("Foo", "orange", (-100, -100), 500)
    print(s3)
    s3.draw()

    win.mainloop()

if __name__ == "__main__":
    main()