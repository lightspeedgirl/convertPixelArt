from xml.etree import ElementTree as ET
import json
from PIL import Image, ImageTk, ImageDraw, ImageFont
from convertPixelArt.models import Threads
import random
import string
import os

def distance(left, right):
    return sum((l-r)**2 for l, r in zip(left, right))**0.5


class NearestColorKey(object):
    def __init__(self, goal):
        self.goal = goal
    def __call__(self, item):
        return distance(self.goal, item[1])



def convertImage(ImageName):
    symbols = []
    originalImage = Image.open(ImageName)
    originalImage.convert('RGB')
    pix = originalImage.load()
    width, hight = originalImage.size 
     #Get the RGBA Value of the a pixel of an image
    pixelsOnImage = list(originalImage.getdata())
    #print pixelsOnImage
    matchedColor = []
    allColorsOnPicture = []


    #Threads.threadID
    #Threads.threadName
    #Threads.red
    #Threads.green
    #Threads.blue
    #Threads.threadHex


    # replace with database
    #fileWithThreadColors = open('C:/Users/Gabriella/Documents/scripting/file.txt', "r")
    #allLinesInfileWithThreadColors = fileWithThreadColors.read()
    #print allLinesInfileWithThreadColors
    #filesDictionary = json.loads(allLinesInfileWithThreadColors)
    #print filesDictionary
    dictonaryWithThreadColor = {}
    listOfHex =[]
    for p in Threads.objects.all():
        threadNameOfColor = str(p.threadID) +'.'+ p.threadName
        dictonaryWithThreadColor[threadNameOfColor] = (p.red , p.green , p.blue)

    #print dictonaryWithThreadColor


    for a in pixelsOnImage:
        allColorsOnPicture.append(min(dictonaryWithThreadColor.items(), key=NearestColorKey(a)))

    #print allColorsOnPicture
    asciiCounter = 33
    for b in allColorsOnPicture:
        matchedColor.append(b[1])


    dmcColorsList = list(set(matchedColor))
    dmcColorsListNames = list(set(allColorsOnPicture))
    dmcColorsListNameOnly = [None] * len(dmcColorsList)
    for d in dmcColorsListNames:
        placement = int(dmcColorsList.index(d[1]))
        dmcColorsListNameOnly[placement] = d[0]

    for a in dmcColorsList:
        if asciiCounter < 127 or asciiCounter > 160:
            symbols.append(chr(asciiCounter))
            asciiCounter+= 1
        elif asciiCounter == 127:
            asciiCounter += 33
            symbols.append(chr(asciiCounter))
    #print dmcColorsList
    #print matchedColor
    #theFile = open("file3.txt","r+")
    #theFile.write('\n'.join('%s %s %s' % x for x in matchedColor))
    newGeneratedImage = Image.new('RGB', (width*32+width-32, hight*32+hight-32), "black")

    #print pixelsOnImage
    currentThreadColor = 0

    draw = ImageDraw.Draw(newGeneratedImage)

    for c in range(0,hight):
        ypos = c*16 + c*16
        for b in range(0,width):
            xpos = b*16 + b*16
            draw.rectangle([(xpos,ypos), (xpos+24,ypos+24)], fill= matchedColor[currentThreadColor])

            symbol = symbols[dmcColorsList.index(matchedColor[currentThreadColor])]
            font = ImageFont.truetype("arial.ttf", 15)
            draw.text((xpos+8, ypos+2), str(symbol), fill=(0, 0, 0), font=font)
            currentThreadColor += 1

    # write to stdout
    randomname = ''.join(random.choice(string.lowercase) for x in range(5))
    newGeneratedImage.save('C:\Users\Gabriella\Documents\scripting\code\mysite\convertPixelArt\static\uploads\converted\\'+ randomname+ ".png")
    randomFile = randomname+ ".png"
    os.remove(ImageName)
    return randomFile, dmcColorsListNameOnly, symbols, dmcColorsList
# for tKinter, replace with html
#    for item in dmcColorsList
#        print item[0]
#        listbox.insert(Tkinter.END, item[0])
#    for a in range(0,len(dmcColorsList)):
#        #print a
#        #print dmcColorsList[a][1]
#        red = hex(dmcColorsList[a][1][0])
#        green = hex(dmcColorsList[a][1][1])
#        blue = hex(dmcColorsList[a][1][2])
#        colorCode = "#{0}{1}{2}".format(red[2:],green[2:],blue[2:])
#        #print "COLOR_CODE: " + colorCode
#        w.create_rectangle(0,15*a+10,15,15*a+25, fill=colorCode ) #Topleft-X, Topleft-Y, Bottomright-X, Bottomright-Y

