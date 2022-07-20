import os

def main():
    openFiles()

def openFiles():
    try:
        with open("myfile2.txt", "r") as f_obj:
            text = f_obj.readlines()
            for lines in text:
                print(text)
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()

