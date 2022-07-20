import os

def main():
    deleteFiles("myfile")

def deleteFiles(name):
    files = os.listdir(os.getcwd())
    for f in files:
        if ".txt" in f:
            os.remove(f)
        if ".zip" in f:
            os.remove(f)
    #

if __name__ == "__main__":
    main()

