import os

def main(num):
    createFiles(num)

def createFiles(num_files):
    with open("myfile.txt", "w") as f_obj:
        f_obj.write("stuff")

if __name__ == "__main__":
    main(input("How many files?"))

