txt_file = open("SetupNewComputer/Modules.txt", "r")

content_list = txt_file.read().splitlines()
print(content_list)