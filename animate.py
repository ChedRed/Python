from PIL import Image, ImageDraw
import os

#<defaults>
width, height = 200, 200
images = []
r, g, b = 255, 0, 0
end = False
offset = 0
#</defaults>
#<parameters>
zoomx = 1
zoomy = 1
barLength = 20
# Zoom is multiplicative
speedx = 1
bandingx = 1
gridding = 1
toSynth = 256
fileExtension = "png"
#</parameters>

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

for i in range(toSynth):
    im = Image.new('RGBA', (width, height), color=(0,0,0,0))
    draw = ImageDraw.Draw(im)
    for l in range(int(height / gridding)):
        while end == False:
            if i * speedx + (l * gridding / zoomy) - offset > 255:
                offset += 256 + bandingx
            else:
                end = True
        r = g = (i) * speedx + int(l * gridding / zoomy) - offset
        offset = 0
        end = False
        for w in range(int(width / gridding)):
            r = 255
            if (r <= 0):
                r = 255
            else:
                r -= int((bandingx) * gridding)
            if (g >= 255):
                g = 0
            else:
                g += int((bandingx) * gridding)
            b = 0
            draw.point((w * gridding, l * gridding), fill=(r, g, int(abs(b))))
    
    clearConsole()
    rendL = ""
    left = str(i)
    
    while len(left) < len(str(toSynth)):
        left = "0" + left
    for r in range(20):
        if r < (i/toSynth)*20:
            rendL += "━"
        else: rendL += "░"
    print("| " + rendL + " |")
    print("Rendered " + left + " / " + str(toSynth) + " Images")
    images.append(im)
clearConsole()
rendL = ""
for r in range(20):
    rendL += "━"
print("| " + rendL + " |")
print("Rendered " + str(toSynth) + " / " + str(toSynth) + " Images")
images[0].save('Desktop/som1didsomething.' + fileExtension, save_all = True, append_images = images[1:])
print("Successfully saved item")