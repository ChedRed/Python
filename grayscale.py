from PIL import Image, ImageDraw
from math import sin, floor
import datetime
import pathlib
import os

#Functions
run="filter" #grayscale, filter
weight="0088FF" #hexadecimal value
effectStr="" #every (number) pixel is affected
opacitE=1 #opacity value from 0.0 to 1.0
opacityType="result" #result, image
#/Functions

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole()
print("Drag and drop file or folder to convert")
input = input("")
time = datetime.datetime.now()
sTimeHr = time.hour
sTimeMn = time.minute
sTimeSc = time.second
sTimeMs = time.microsecond
inputF=""

#-=-=-=-Image Editor-=-=-=-#

def processImage(filePath, printText):
    with Image.open(filePath) as toProcess:
        toProcess.load()
    toProcess = toProcess.convert("RGBA")
    length=toProcess.size[1]
    width=toProcess.size[0]
    draw = ImageDraw.Draw(toProcess)
    effect=""
    value=0
    valueStr=""
    getValue=0
    for i in range(len(effectStr)):
        if effectStr[i] != " ":
            if getValue == 0:
                effect+=effectStr[i]
            else:
                valueStr+=effectStr[i]
        else:
            getValue=1
    if len(effectStr) > 0:
        value=int(valueStr)
    for l in range(length):
        for w in range(width):
            pixel = toProcess.getpixel((w,l))
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]
            p=pixel[3]
            rW=((int(weight[0], 16)*16)+int(weight[1], 16))/255
            gW=((int(weight[2], 16)*16)+int(weight[3], 16))/255
            bW=((int(weight[4], 16)*16)+int(weight[5], 16))/255
            if run=="grayscale":
                c=int((0.299*r)+(0.587*g)+(0.114*b))
                if opacityType=="result":
                    rR=int((((c*rW)-rW)*opacitE)+rW)
                    gR=int((((c*gW)-gW)*opacitE)+gW)
                    bR=int((((c*bW)-bW)*opacitE)+bW)
                elif opacityType=="image":
                    rR=int((((c*rW)-r)*opacitE)+r)
                    gR=int((((c*gW)-g)*opacitE)+g)
                    bR=int((((c*bW)-b)*opacitE)+b)
            elif run=="filter":
                rR = int(r*rW)
                gR = int(g*gW)
                bR = int(b*bW)
            if effect=="every":
                if floor(sin((w+l)/4))%value==0: draw.point((w,l), fill=(rR,gR,bR,p))
            else: draw.point((w,l), fill=(rR,gR,bR,p))
        if printText:
            clearConsole()
            rendL = ""
            left=str(floor((l/length)*100))
            while len(left) < 3:
                left = "0" + left
            for r in range(15):
                if r < (l/length)*15: rendL += "━"
                else: rendL += "░"
            print("| " + rendL + " |")
            print("|  Rendered " +left+"%  |")
    toProcess.save(filePath)

def getCompletionTime():
    time2 = datetime.datetime.now()
    nTimeHr = time2.hour - sTimeHr
    nTimeMn = time2.minute - sTimeMn
    nTimeSc = time2.second - sTimeSc
    nTimeMs = time2.microsecond - sTimeMs
    timeMessage=""
    if nTimeMn < 0:
        nTimeHr -= 1
        nTimeMn += 60
    if nTimeSc < 0:
        nTimeMn -= 1
        nTimeSc += 60
    if nTimeMs < 0:
        nTimeSc -= 1
        nTimeMs += 1000000
    if nTimeHr > 0:
        timeMessage += str(nTimeHr) + " Hours, "
    if nTimeMn > 0:
        timeMessage += str(nTimeMn) + " Minutes, "
    timeMessage += str(nTimeSc) + " Seconds, "
    timeMessage += "and " + str(nTimeMs) + " Microseconds."
    return timeMessage
#-=-=-=-Main Code-=-=-=-#

if not os.path.exists(input):
    print("ERROR: Does not exist")
if os.path.isfile(input):
    processImage(input, True)
    clearConsole()
    print("Succesfully converted image to grayscale")
    print("Operation took " + getCompletionTime())
else:
    toSynth = 0
    completed = 0
    for path, subdirs, files in os.walk(input):
        for name in files:
            if pathlib.Path(os.path.join(path, name)).suffix == ".png":
                toSynth+=1
    for path, subdirs, files in os.walk(input):
        for name in files:
            if pathlib.Path(os.path.join(path, name)).suffix == ".png":
                clearConsole()
                completed += 1
                rendL = ""
                left=str(completed)
                while len(left) < len(str(toSynth)):
                    left = "0" + left
                for r in range(15+(len(str(toSynth))*2)):
                    if r < ((completed/toSynth)*15+(len(str(toSynth))*2)-1):
                        rendL += "━"
                    else: rendL += "░"
                print("| " + rendL + " |")
                print("|  Converted " + left + " / " + str(toSynth)+"  |")
                print("")
                print("Converting " + os.path.join(path, name))
                processImage(os.path.join(path, name), False)
    rendL = ""
    for r in range(15+(len(str(toSynth))*2)):
        rendL += "━"
    print("| " + rendL + " |")
    print("|  Converted " + str(toSynth) + " / " + str(toSynth) +"  |")
    print("successfully converted "+str(toSynth)+" images to grayscale.")
    print("Operation took " + getCompletionTime())
