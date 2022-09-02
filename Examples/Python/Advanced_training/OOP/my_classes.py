from turtle import Turtle

class Shape:
    """ This is a shape class. """
    
    # Class Variables
    general_type = "Polygon"

    def __init__(self, name, color, location, length):
        self.name = name
        self.location = location
        self.length = length
        self.t = Turtle()
        self.t.speed(0)
        self.t.color(color)
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(location)

    def draw(self):
        """Draws the shape if possible..."""

        print("I can't draw :'(")
    
    def __str__(self):
        return f"This is a {str(self.__class__).split('.')[-1][:-2]}..."


class Square(Shape):
    """Creates a square."""

    def __init__(self, name, color, location, length):
        super().__init__(name, color, location, length)

    def draw(self):
        self.t.pendown()
        for side in range(4):
            self.t.forward(self.length)
            self.t.right(90)
        self.t.penup()

class Triangle(Shape):
    """Creates a square."""

    def __init__(self, name, color, location, length):
        super().__init__(name, color, location, length)

    def draw(self):
        self.t.pendown()
        for side in range(3):
            self.t.forward(self.length)
            self.t.right(120)
        self.t.penup()
