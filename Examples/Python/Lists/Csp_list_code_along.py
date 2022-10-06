
#Declare and Initialize an empty list
Listy_mcListface = []

#Declare and Initialize a list with starting values
list_o_stuff =["stuff","things"]

#lists can hold lots of types of things
jimmy = "old"
tacos_are_good = True
another_list= [42,7]
more_stuff = [jimmy,tacos_are_good,True,12,43,"orange",another_list]

print(more_stuff)

#Some List Functions
print(more_stuff[0])                #Access an index
print(more_stuff[0:3])              # access a slice of indexes
more_stuff.append("two")            #append (add to the end)
more_stuff.append(jimmy)            #append (add to the end)
more_stuff.append(list_o_stuff)     #append (add to the end) another list
print(more_stuff)
more_stuff.append(list_o_stuff[1])
print(more_stuff)

# for loop over a list + Pop
count = 0
for i in more_stuff:
    print(i)
    i = count
    count = count+1
    print(count)


length = len(more_stuff)
for i in range(length):
    popper = more_stuff.pop()
    print(popper, "was on top... gone now though!\n")
    
    if not isinstance(i,bool):    
        if isinstance(i,int):
            if i % 2==0:
                print("even")
            else:
                print("odd")
        else:
            print("That's not a number silly")
    else:
            print("That's not a number silly")

print("list emptied but not deleted", more_stuff)

#Make a list from user input
user_list = []
length = int(input("How many items to you want to put on the list?"))

for i in range(length):
    print("*"*20)
    user_input = input("What do you want to add?:\n\n")
    user_list.append(user_input)
    
    print(f"\nI added {user_input}, the new list is:\n {user_list}\n")


#Remove an item from a list
user_list.remove(user_input)
print("removed",user_input)
print(user_list)

user_list.reverse()
print("reversed the list")
print(user_list)

user_list.insert(2,"tacos")
print(user_list)

user_list.sort()
print(user_list)

print("done")