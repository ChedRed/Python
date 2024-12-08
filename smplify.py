from PIL import Image, ImageDraw
from math import floor
from playsound import playsound
import datetime
import pathlib
import os

#Functions
every=32 #number of 'bits'
AdvancedFunction=1 #0 is off, 1 is normal, 2 is corrupt
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
for i in range(len(input)-2):
    inputF+=input[i+1]
input=inputF

#-=-=-=-Image Editor-=-=-=-#

def roundEvery(value, every):
    return every * floor(value/every)

def roundEveryCorrupt(value, valueUp, valueDown, valueLeft, valueRight, every):
    target=every * floor(value/every)
    incOrDecNumber=0
    if valueUp!=1:
        Uppards=every * floor(valueUp/every)
    else:
        Uppards=-1
    if valueDown!=1:
        Downards=every * floor(valueDown/every)
    else:
        Downards=-1
    if valueLeft!=1:
        Leftards=every * floor(valueLeft/every)
    else:
        Leftards=-1
    if valueRight!=1:
        Rightards=every * floor(valueRight/every)
    else:
        Rightards=-1
    if target-every==Uppards:
        incOrDecNumber-=1
    elif target+every==Uppards:
        incOrDecNumber+=1
    if target-every==Downards:
        incOrDecNumber-=1
    elif target+every==Downards:
        incOrDecNumber+=1
    if target-every==Leftards:
        incOrDecNumber-=1
    elif target+every==Leftards:
        incOrDecNumber+=1
    if target-every==Rightards:
        incOrDecNumber-=1
    elif target+every==Rightards:
        incOrDecNumber+=1
    if incOrDecNumber > 0:
        target+=every
    if incOrDecNumber < 0:
        target-=every
    return target

def processImage(filePath, printText):
    with Image.open(filePath) as toProcess:
        toProcess.load()
    if AdvancedFunction<2:
        with Image.open(filePath) as Processed:
            Processed.load()
        Processed = Processed.convert("RGBA")
    toProcess = toProcess.convert("RGBA")
    length=toProcess.size[1]
    width=toProcess.size[0]
    if AdvancedFunction>1:
        draw = ImageDraw.Draw(toProcess)
    else:
        draw = ImageDraw.Draw(Processed)
    for l in range(length):
        for w in range(width):
            pixel = toProcess.getpixel((w,l))
            if AdvancedFunction>0:
                if length-1 > l:
                    pixelUp=toProcess.getpixel((w,l-1))
                else:
                    pixelUp = -1
                if length+1 < l:
                    pixelDown=toProcess.getpixel((w,l+1))
                else:
                    pixelDown = -1
                if width-1 > w:
                    pixelLeft=toProcess.getpixel((w-1,l))
                else:
                    pixelLeft = -1
                if width+1 < w:
                    pixelRight=toProcess.getpixel((w+1,l))
                else:
                    pixelRight=-1
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]
            p=pixel[3]
            if AdvancedFunction>0:
                if pixelUp!=-1:
                    rU=pixelUp[0]
                    gU=pixelUp[1]
                    bU=pixelUp[2]
                else:
                    rU=-1
                    gU=-1
                    bU=-1
                if pixelDown!=-1:
                    rD=pixelDown[0]
                    gD=pixelDown[1]
                    bD=pixelDown[2]
                else:
                    rD=-1
                    gD=-1
                    bD=-1
                if pixelLeft!=-1:
                    rL=pixelLeft[0]
                    gL=pixelLeft[1]
                    bL=pixelLeft[2]
                else:
                    rL=-1
                    gL=-1
                    bL=-1
                if pixelRight!=-1:
                    rR=pixelRight[0]
                    gR=pixelRight[1]
                    bR=pixelRight[2]
                else:
                    rR=-1
                    gR=-1
                    bR=-1
                r=roundEveryCorrupt(r, rU, rD, rL, rR, every)
                g=roundEveryCorrupt(g, gU, gD, gL, gR, every)
                b=roundEveryCorrupt(b, bU, bD, bL, bR, every)
            else:
                r=roundEvery(r, every)
                g=roundEvery(g, every)
                b=roundEvery(b, every)
            draw.point((w,l), fill=(r,g,b,p))
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
    if AdvancedFunction>1:
        toProcess.save(filePath)
    else:
        Processed.save(filePath)

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

if os.path.isfile(input):
    processImage(input, True)
    clearConsole()
    print("Succesfully converted image bits.")
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
    
    for r in range(15+(len(str(toSynth))*2)):
        rendL += "━"
    print("| " + rendL + " |")
    print("|  Converted " + str(toSynth) + " / " + str(toSynth) +"  |")
    clearConsole()
    playsound("/Users/ryanchou/Desktop/ /Programs/Resources/Ping.wav")
    print("successfully converted "+str(toSynth)+" images bit.")
    print("Operation took " + getCompletionTime())