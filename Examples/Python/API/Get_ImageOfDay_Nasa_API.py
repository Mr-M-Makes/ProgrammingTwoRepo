import ctypes
import struct
import requests
import json
import shutil # to save it locally
import os

def get_key():
    text = open("Keys\\nasa.txt", "r")
    key = text.read()
    text.close()
    return key


def main():
    #Set Up Api Call
    url = "https://api.nasa.gov/planetary/apod"
    api_key = get_key()
    query_params = { "api_key": api_key, "count":1, "hd":True }

    #Make API Call
    response = requests.get(url, query_params).json()
    print(response)

    #Save Response as file
    with open('personal.json', 'w') as json_file:
        json.dump(response, json_file)

    #Open Json File saved
    f = open('personal.json')
  
    # returns JSON object as a dictionary
    data = json.load(f)
    
    #save download url
    Download = data[0]['url']
    
    #print(Download) #Debug Check

    #Name File
    filename = Download.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(Download, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived') # Error code

    #Set current Working Directory as path and concatenate filename
    path = os.getcwd() + "\\Images\\" + filename
    
    #print(path)    #debug Check
    
    #set image to desktop background
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)


#Call Function main
main()