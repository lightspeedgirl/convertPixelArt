from PIL import Image, ImageDraw

im = Image.open(r"C:\Users\light\Pictures\354894-95f9b-86963058--ua8674 - Copy.jpg")
width, height = im.size
draw = ImageDraw.Draw(im)

newLinePos = 0
while(newLinePos < width):
    draw.line((0, newLinePos, im.size[0], newLinePos), fill=000)
    newLinePos+=5
    
newLinePosx = 0

while(newLinePosx < width):
    draw.line((newLinePosx, 0, newLinePosx, im.size[1]), fill=000)
    newLinePosx+=4
    

# draw.line((50, 50) + im.size, fill=128)
del draw

# write to stdout
im.save(r'C:\Users\light\Pictures\test002.png')