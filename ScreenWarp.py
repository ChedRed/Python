#---System---#
import pyautogui as pgi
import os
pgi.FAILSAFE = False
#---Editables---#
shiftTime = 0.005
deferr = 1
EdgeTimeMax = 0
xMax = 1679
yMax = 1049
#---PreSet---#
err = deferr
timeAtEdge = EdgeTimeMax
#----------------------------------------------------#
while True:
    os.system('clear')
    if (pgi.position()[0] < err):
        if timeAtEdge <= 0:
            pgi.moveTo(xMax - err, pgi.position()[1])
            timeAtEdge = EdgeTimeMax
        else:
            timeAtEdge -= shiftTime
    elif (pgi.position()[0] > xMax - err):
        if timeAtEdge <= 0:
            pgi.moveTo(err, pgi.position()[1])
            timeAtEdge = EdgeTimeMax
        else:
            timeAtEdge -= shiftTime
    elif (pgi.position()[1] < err):
        if timeAtEdge <= 0:
            pgi.moveTo(pgi.position()[0], yMax - err)
            timeAtEdge = EdgeTimeMax
        else:
            timeAtEdge -= shiftTime
    elif (pgi.position()[1] > yMax - err):
        if timeAtEdge <= 0:
            pgi.moveTo(pgi.position()[0], err)
            timeAtEdge = EdgeTimeMax
        else:
            timeAtEdge -= shiftTime
    else:
        timeAtEdge = EdgeTimeMax
    print(str(timeAtEdge))
#----------------------------------------------------#