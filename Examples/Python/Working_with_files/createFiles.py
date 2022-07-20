import os

def main(num):
    createFiles(num)

def createFiles(num_files):
    num = 1
    for nums in range(num_files): 
        filename = "myfile" + str(num+1) + ".txt"
        with open(filename, "w") as f_obj:
            f_obj.write("stuff")
        num += 1
if __name__ == "__main__":
    main(int(input("How many files?")))

