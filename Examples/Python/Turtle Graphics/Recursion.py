def recursive_divide_by_x (n,x):
    if (n > x ** 2):
    
        n = recursive_divide_by_x(n // x , x)
        
    else:
        print (n)

n = int(input("n = \n"))
x = int(input("x = \n"))

recursive_divide_by_x(n,x)
print(n)