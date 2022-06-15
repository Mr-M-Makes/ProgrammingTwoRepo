
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



import random   #import allows us to use functions other people have created
count=0         #python declares and initializes variables in one step
x=0             
trials=[]
while x<42:
    trials.append(x)
    x += random.randint(1,5)
    count +=1
print("Hello, This took ",count," iterations")
print("They were: ",trials)
print("More Stuff")