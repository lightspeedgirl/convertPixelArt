from PIL import Image, ImageTk, ImageDraw, ImageFont
import math
import random
import numpy as np
def getDominantColor( xy, n, image):
    count = 0
    pixelsInTheSquare = []
    for s in range(xy[0], xy[0]+n+1):
        for t in range(xy[1], xy[1]+n+1):
            # pixlr, pixlg, pixlb = image[s, t]
            pixelsInTheSquare.append("_".join(map(str, image[s, t])))
            # print(image[s,t])
    a, b, c = np.unique(pixelsInTheSquare, return_index=True, return_counts=True)

    r, g, b = pixelsInTheSquare[max(b)].split("_")
    return ((int(r)), (int(g)), (int(b)))

def get_average_color( xy, n, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
 
    r, g, b = 0, 0, 0
    count = 0
    for s in range(xy[0], xy[0]+n+1):
        for t in range(xy[1], xy[1]+n+1):
            pixlr, pixlg, pixlb = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    return ((r/count), (g/count), (b/count))
 
# image = Image.open('test.png').load()
# r, g, b = get_average_color((24,290), 50, image)
# print r,g,b


sizeOfPixel = 5
originalImage = Image.open(r"C:\Users\light\Pictures\354894-95f9b-86963058--ua8674.jpg")
funcImage = Image.open(r"C:\Users\light\Pictures\354894-95f9b-86963058--ua8674.jpg").load()
originalImage.convert('RGB')
pix = originalImage.load()
width, height = originalImage.size 
pixelClustersSizeMax = math.ceil(max(width, height))
pixelClustersSizeMin = math.ceil(min(width, height))
colors = []
i = 0
j = 0
while(i != pixelClustersSizeMin):
    if((i+sizeOfPixel*2 > pixelClustersSizeMin)):
        break
    while(j != pixelClustersSizeMax):
        if(j+sizeOfPixel*2 > pixelClustersSizeMax):
            break
        # r, g, b = get_average_color((j,i), sizeOfPixel, funcImage)
        r, g, b = getDominantColor((j,i), sizeOfPixel, funcImage)
        colors.append((math.ceil(r),math.ceil(g),math.ceil(b)))
        # print(i, j)
        # print (r,g,b)        
        j +=sizeOfPixel
    i +=sizeOfPixel
    j = 0
# print(colors)

newGeneratedImage = Image.new('RGBA', ( ( math.ceil( (width/sizeOfPixel) *(sizeOfPixel+2)) ), (math.ceil((height/sizeOfPixel)*(sizeOfPixel+2))) ), color='#000000')
draw = ImageDraw.Draw(newGeneratedImage)

ypos = 0
xpos = 0
currentThreadColor = 0
for y in range(math.ceil((height-sizeOfPixel*2)/sizeOfPixel)):  
    for x in range(math.ceil((width-sizeOfPixel*2)/sizeOfPixel)):
        if(currentThreadColor !=  ((len(colors))-1)):             
            draw.rectangle([(xpos,ypos), (xpos+sizeOfPixel,ypos+sizeOfPixel)], fill = colors[currentThreadColor])
            # print(colors[currentThreadColor])
            currentThreadColor += 1
            xpos += sizeOfPixel+2
    ypos += sizeOfPixel+2
    xpos = 0


newGeneratedImage.save(r'C:\Users\light\Pictures\test.png')
# randomFile = randomname+ ".png"


#Get the RGBA Value of the a pixel of an image
# pixelsOnImage = list(originalImage.getdata())
# print (pixelsOnImage)