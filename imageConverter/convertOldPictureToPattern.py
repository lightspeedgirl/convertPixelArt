from PIL import Image, ImageTk, ImageDraw, ImageFont
import math
import random
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
while(i != pixelClustersSizeMax):
    if((i+10 > pixelClustersSizeMax)):
        break
    while(j != pixelClustersSizeMin):
        if(j+10 > pixelClustersSizeMin):
            break
        r, g, b = get_average_color((i,j), 5, funcImage)
        colors.append((math.ceil(r),math.ceil(g),math.ceil(b)))
        # print(i, j)
        # print (r,g,b)        
        j +=5
    i +=5
    j = 0
# print(colors)

newGeneratedImage = Image.new('RGBA', (width, height), color='#000000')
draw = ImageDraw.Draw(newGeneratedImage)

ypos = 0
xpos = 0
currentThreadColor = 0
for y in range(height):  
    for x in range(width):
        if(currentThreadColor != ((len(colors))-1)):             
            draw.rectangle([(xpos,ypos), (xpos+5,ypos+5)], fill = colors[currentThreadColor])
            print(colors[currentThreadColor])
            currentThreadColor += 1
            xpos += 6
    ypos += 6
    xpos = 0


newGeneratedImage.save(r'C:\Users\light\Pictures\test.png')
# randomFile = randomname+ ".png"


#Get the RGBA Value of the a pixel of an image
# pixelsOnImage = list(originalImage.getdata())
# print (pixelsOnImage)