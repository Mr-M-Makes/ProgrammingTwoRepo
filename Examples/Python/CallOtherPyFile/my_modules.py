from turtle import Turtle, color
class Shape:
    general_type = "Polygon"    #Class Variable
    def __init__(self, name):
        self.name = name


class Rectangle:
    """This is a shape class. You put a shape name here."""
    
    general_type = "4 sided shape"    #Class Variable

    def __init__(self,name, length, width) -> None:
        self.length = length
        self.width = width
        self.name = name
        self.t = Turtle()
        self.t.speed(0)
        pass

    def print_shape(self):
        print(self.name)

    def ask_shape(self):    
        pass

    def draw_shape(self):

        pass



class Square(Rectangle):
    def __init__(self, name, length) -> None:
        super().__init__(name, length, length)

    def draw_shape(self):
        self.t.pendown()
        for side in range (4):    
            self.t.forward(self.length)
            self.t.right(90)
       



def main():
    pass

if __name__ == "__main__":
    main()