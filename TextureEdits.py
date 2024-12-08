from PIL import Image, ImageDraw
import os

#<parameters>
Grayscale = True
Bias = 0
gridding = 1
Mr, Mg, Mb = 1, 1, 1
fileExtension = "png"
#</parameters>

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

clearConsole()
print("Drag and drop file or folder to convert")
input = input("")
inputF = ""
for i in range(len(input)-2):
    inputF += input[i+1]
input = inputF
#--------
#--------
SetImage = Image.open(input)
draw = ImageDraw.Draw(SetImage)
width = SetImage.width
height = SetImage.height

for l in range(height):
    for w in range(width):
        pixel = SetImage.getpixel((w,l))
        r = int(pixel[0])
        g = int(pixel[1])
        b = int(pixel[2])
        p = int(pixel[3])
        e = 255 - int(abs(r-g) + abs(r-b) + abs(g-b) / 2)
        Er = Mr
        Eg = Mg
        Eb = Mb
        c = int((0.299*r)+(0.587*g)+(0.114*b))
        if Bias > 0:
            Er = 1 - (Mr * ((255 - e) / 255))
            Eg = 1 - (Mg * ((255 - e) / 255))
            Eb = 1 - (Mb * ((255 - e) / 255))
        if Bias == 1:
            r = int(Er * pixel[0])
            g = int(Eg * pixel[1])
            b = int(Eb * pixel[2])
        elif Bias == 2:
            r = int(Er * c)
            g = int(Eg * c)
            b = int(Eb * c)
        if (w + l) % gridding == 0:
            if Grayscale:
                c = int((0.299*r)+(0.587*g)+(0.114*b))
                draw.point((w, l), fill=(c, c, c, p))
            else:
                draw.point((w, l), fill=(r, g, b, p))
    
    clearConsole()
    rendL = ""
    left = str(i)

clearConsole()
rendL = ""
for r in range(20):
    rendL += "━"
print("| " + rendL + " |")
SetImage.save(input)
print("Successfully saved item to " + str(input))