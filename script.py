#!/usr/bin/python

#Created by Conor Amanatullah, 2016

# This script will pull a random image from unsplash and set it as the desktop background


import os
import sys
import random
import urllib

def changeBackground(size):

        print("Resolution: "+ size)
        print("Downloading image...")
        urllib.urlretrieve("https://source.unsplash.com/random/"+size, "image.jpg")
        print("Background changed.")
        os.system("gsettings set org.gnome.desktop.background picture-uri 'file:/home/conor/unsplash-script/image.jpg'")


def setup():
    f = open('settings.txt', 'wb')
    newSize = raw_input("Please enter your current screen size in the format widthXheight: ")
    f.write(newSize)

def startup():
    f = open('settings.txt', 'r+')
    savedSize = f.readline()
    urllib.urlretrieve("https://source.unsplash.com/random/"+savedSize, "image.jpg")
    os.system("gsettings set org.gnome.desktop.background picture-uri 'file:/home/conor/unsplash-script/image.jpg'")

def save():
    save = raw_input("Would you like to save the current background? (Y/N): ")
    if save == "Y":
        name = random.randrange(100)
        name = str(name)
        os.system("cp image.jpg saved/" + name + ".jpg")
        print("Image saved to 'saved' folder as " + name + ".jpg")
    else:
        print("Ok then...")
        quit()

if (len(sys.argv) > 1):
    if(sys.argv[1] == "setup"):
        setup()
    elif(sys.argv[1] == "startup"):
        startup()
    elif(sys.argv[1] == "save"):
        save()
else:
    if(os.path.isfile("settings.txt")):
        f = open('settings.txt', 'r')
        size = f.readline()
        changeBackground(size)
    else:
        print("Please run using ./script.py setup first!")
        quit()
