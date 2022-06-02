import random
count=0
x=0
trials=[]
while x<42:
    trials.append(x)
    x += random.randint(1,5)
    count +=1
print("Hello, This took ",count," iterations")
print("They were: ",trials)
