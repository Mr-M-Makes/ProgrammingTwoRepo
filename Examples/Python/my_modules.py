

from unicodedata import name


class Shape:
    """This is a shape class. You put a shape name here."""
    
    general_type = "Polygon"    #Class Variable

    def __init__(self, shape) -> None:
        self.name = shape

    def print_shape(self):
        print(self.name)


def main():
    pass

if __name__ == "__main__":
    main()