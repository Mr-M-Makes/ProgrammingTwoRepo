import os
from zipfile import ZipFile, is_zipfile

def main():
    UnZipFiles()

def UnZipFiles():
    for file in os.listdir(os.getcwd()):
        if is_zipfile(file):
            UnZipFiles(file)
        



if __name__ == "__main__":
    main()

