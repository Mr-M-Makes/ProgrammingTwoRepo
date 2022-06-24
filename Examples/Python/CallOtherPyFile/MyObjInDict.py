from numpy import true_divide


Objects = {}
close = False
#Functions
def new_object():
    Trait1 = input("What is your 1st trait? ")
    Trait2 = input("What is your 2nd trait? ")
    Trait3 = input("What is your 3rd trait? ")
    print("\n")
    Objects[Trait1] = MyObj_class_example(Trait1, Trait2, Trait3)

def list_Trait1():
    Trait1List = Objects.keys()
    print(Trait1List)
    return Trait1List

def show_dict():
    nameList = [i for i in Objects]
    num = 1

    for x in nameList:
        print(num, ") ", x)
        num += 1

    pickFromList = int(input("Choose from list please "))
    print("")
    nameList = list(nameList)
    index_key = pickFromList - 1
    Objects[nameList[index_key]].say_hi()

def Menu():
    Objects = {}
    close = False
    while close == False:
        print("1)Add object\n2)Show Object Data\n3)Close Program")
        task = input("What do you want to do? ")
        if task.isdigit():
            task = int(task)
            if task == 1:
                new_object()
            elif task == 2:
                show_dict()
            elif task == 3:
                confirm = input("Are you sure? Type 'CONFIRM' to lose everything.")
                if confirm == "CONFIRM":
                    close = True
        else:
            print("Please choose a number.\n")

class MyObj_class_example:  
        
    def __init__(self, first, second, third):  
        self.f = first  
        self.s = second
        self.th = third
        
    
    def __str__(self):
        return str(self.values)
  
    def say_hi(self):  
        print('Hello, my 1st trait is', self.f, "\n") 
        #print('My weight is nunya beeswax', "\n")
        print('My 2nd trait is ', self.s, "\n") 
        print('My 3rd trait is ', self.th, "\n")  


