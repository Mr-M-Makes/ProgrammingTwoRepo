

def convert_dec(number):
    """number must be integer"""
    placeValue = 4096
    Convert_dictionary ={}

    subtract_place_value(number,place_value_list,Convert_dictionary)
    print(Convert_dictionary)

def subtract_place_value(number,placevalue,Convert_dictionary):
    print("number = ", str(number))
    print("placevalue = ", str(placevalue))
    if (number-placevalue) >= 0:
        updater = {placevalue:1}
        print(updater)
        Convert_dictionary.update(updater)
        number = number - placevalue
        return number,placevalue,Convert_dictionary


convert_dec(87)
