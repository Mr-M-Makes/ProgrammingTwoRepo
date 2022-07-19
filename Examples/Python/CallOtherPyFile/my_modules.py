

from unicodedata import name


class Shape:
    """This is a shape class. You put a shape name here."""
    
    general_type = "Polygon"    #Class Variable

    def __init__(self, shape) -> None:
        self.name = shape 

    def print_shape(self):
        print(self.name)

    def num_anlges(self):

 
        
def ask_shape():    
    questions = [
    inquirer.List('Chosen_Shape',
                    message="What Shape do you have?",
                    choices=['Square', 'Circle', 'Triangle', 'Pentagon', 'Hexagon'],
                ),
    ]
    answers = inquirer.prompt(questions)
    print answers["size"]

def main():
    pass

if __name__ == "__main__":
    main()