from turtle import Screen

import MyObjInDict as f 
import my_modules 


def Choose_program():
    close = False
    while close == False:
        print("1)Play Shapes\n2)Show Object Data\n3)Close Program")
        task = input("What do you want to do? ")
        if task.isdigit():
            task = int(task)
            if task == 1:
                Play_Shapes()
            elif task == 2:
                f.new_object()
                f.Menu()
            elif task == 3:
                confirm = input("Are you sure? Type 'CONFIRM' to lose everything.")
                if confirm == "CONFIRM":
                    close = True
        else:
            print("Please choose a number.\n")

def Play_Shapes():
    shape = input("Input a shape = ")
    if shape == "square" or shape == "Square":
        length = int(input("Length = "))
        color = input("Color = ")
        shape1 = my_modules.Square(shape, length)
        main()
        shape1.draw_shape()
    elif shape == "Rectangle" or shape == "rectangle":
        length = int(input("Length = "))
        width = int(input("Width = "))
        color = input("Color = ")
        shape1 = my_modules.Rectangle(shape, length, width)
        main()
        shape1.draw_shape()
        
    else:
        shape1 = my_modules.Shape(shape)

    #shape1.ask_shape()  # deprecated function - so double comment becuase if I bring it back this second comment will stay a comment


def main():
    win = Screen()
    win.setup(800,700)
    win.colormode(255)
    win.bgcolor((34,56,74))




Choose_program()