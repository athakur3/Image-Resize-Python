#!/usr/bin/python
from PIL import Image
import os, sys

path = "path to your directory that contains images"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            kbSize = os.path.getsize(path+item)/1000
            print(kbSize)
            im = Image.open(path+item)
            (width, height) = im.size
            
            while kbSize > 200:   

                print(path+item)

                if os.path.exists(path + item + 'resized.jpg'):
                    os.remove(path + item + 'resized.jpg')
                else:
                    print("The file does not exist")

                (newWidth, newHeight) = (int(width * 0.9), int(height * 0.9)) 
                imResize = im.resize((newWidth, newHeight), Image.ANTIALIAS)
                imResize.save(path + item + 'resized.jpg', 'JPEG', quality=90)
                kbSize = os.path.getsize(path + item + 'resized.jpg')/1000
                print(kbSize)
                (width, height) = imResize.size
            else:
                if os.path.exists(path + item):
                    os.remove(path + item)
                else:
                    print("The file does not exist")

resize()
