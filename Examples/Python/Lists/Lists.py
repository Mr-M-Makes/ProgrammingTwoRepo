import random
grades = []

lots_o_grades = [42,65,76,90,100]

jerry = "old"
fried_rice_is_good = True
jimmy = "old"
tacos_are_good = True
another_list= [42,7]
more_stuff = [jimmy,tacos_are_good,True,12,43,"orange",another_list]

print(more_stuff)
randnum= random.randint(0,len(more_stuff)-1)
print(len(more_stuff))
print(randnum)
print(more_stuff[randnum])

print(more_stuff[0:3])

more_stuff.append("apple")
apple = "good"
more_stuff.append(apple)
more_stuff.append(lots_o_grades)
print(more_stuff)
more_stuff.insert(3,"z")
print(more_stuff)

length = len(more_stuff)
for i in range(length):
    popper = more_stuff.pop()
    print(popper, "was on top... gone now though!\n")
print("list emptied but not deleted", more_stuff)

user_list =[]
length = int(input("how many things you got there man?"))

for i in range(length):
    things = input("what are we putting in the list?\n")
    user_list.append(things)
    print(f"\nI added {things}, the new list is:\n {user_list}\n")

user_list.remove(things)
print("removed",things)
print(user_list)

user_list.reverse()
print("reversed the list")
print(user_list)

user_list.insert(2,"tacos")
print(user_list)

user_list.sort()
print(user_list)

print("done")