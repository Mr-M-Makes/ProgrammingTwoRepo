      #----------------------------------------------------------------------------
      # Created By  : Blake Matthews - Programming 2
      # Created Date:       6/15
      # Project Name:       1st Python Example
      # Project Purpose:    Teach Student Intoductory Python
      # Project Function:   Prints 42 random numbers 
      # ---------------------------------------------------------------------------
      # Psuedocode:
      #
      # import Modules
      # set count and x to 0
      # create a blank list
      # print 42 random numbers with some pretty output text
      # end
      # 
      # ---------------------------------------------------------------------------

"""#import needed modules - You can delete the # from the following lines for common ones installed on lab pcs
                            This is a multiline string. It is considered bad programming. Don't do this without 
                            a reason. I did it here to make these show a different color if our linter is turned
                            on. They can be used to make multiline comments"""
#import random              #random number generator
#import numpy               #work with arrays and random numbers - much better than built in list
#import matplotlib          #make graphs
#import pillow              #work with images
#import pendulum            #replaces built in datetime
#import moviepy             #work with video
#import tkinter             #gui maker
#import requests            #use with APIs
#import pygame              #make games
#import turtle              #draw shapes



"""initialize global variables_______________________________________________________________________"""
#int = 65           #Variable int is defined and assigned. It is an Integer
#float = 65.0       #Float
#string = "65"      #String
#bool = True        #Boolean
people = {}


"""define functions here - They can be put in different places... but unless you have a good reason put it here"""
#def my_function1(x,y):
    #if x < y:
        #print(x + "is greater than " + y)          #make sure to remember the extra space when concatendating
    #else print("Why u so BIG Y")

def new_person():
    name = input("What is your name?")
    height = input("What is your height?")
    eyeColor = input("What is your eye color?")
    people[name] = Person(name, height, eyeColor)

def list_names():
    nameList = people.keys()
    print(nameList)
    return nameList

def show_dict():
    print(people.items())
    

"""Write your classes for your program here"""

# A Sample class with init method  
class Person:  
      
    # init method or constructor   
    def __init__(self, name, h, ec):  
        self.name = name  
        self.h = h
        self.ec = ec

    # Sample Method   
    def say_hi(self):  
        print('Hello, my name is', self.name) 
        print('My weight is nunya beeswax')
        print('My height is ', self.h) 
        print('My eyes are ', self.ec)  

      


"""Write the main body of your program here"""
while 1 > 0:
    new_person()
    #list = list_names()
    show_dict()
    pickFromList = input("choose from list please")
    #choice = pickFromListj
    #print(choice)
    people[pickFromList].say_hi()
