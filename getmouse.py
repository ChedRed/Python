import pyautogui as pgi
import os
pgi.FAILSAFE = False
xMin = 0
xMax = 0
yMin = 0
yMax = 0
while True:
    os.system('clear')
    if (pgi.position()[0] < xMin):
        xMin = pgi.position()[0]
    if (pgi.position()[0] > xMax):
        xMax = pgi.position()[0]
    if (pgi.position()[1] < yMin):
        yMin = pgi.position()[1]
    if (pgi.position()[1] > yMax):
        yMax = pgi.position()[1]
    print('xMin = '+str(xMin))
    print('xMax = '+str(xMax))
    print('yMin = '+str(yMin))
    print('yMax = '+str(yMax))