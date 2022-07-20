import os
from zipfile import ZipFile

def main(ext):
    ZipFiles(ext)

def ZipFiles(ext):
    for file in os.listdir(os.getcwd()):
        if  file.endswith(ext):
            filename = f"{file[:-4]}.zip"
            with ZipFile(filename, "w") as zip:
                zip.write(file)
            os.remove(file)



if __name__ == "__main__":
    main(input("What extention of files?"))

