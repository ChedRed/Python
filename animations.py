import os
import pygame
import PIL
import datetime
import pygame.gfxdraw
from math import *

from libraries import overground

oscommands = overground.oscommands()
errhandler = overground.errhandles()

oscommands.clearConsole()

size = input("Insert a coordinate for the window size\n")
canvas = input("Insert a coordinate for the canvas (must be larger than window size):\n")
multiplier = int(input("Insert the size of each pixel per pixel:\n"))

start = datetime.datetime.now()

if size:
    tempa = ""
    tempb = ""
    temp = False
    for i in range(len(size)):
        if size[i] in "1234567890,":
            if size[i] == ",":
                temp = True
            elif temp:
                tempb += size[i]
            else:
                tempa += size[i]
    if not (tempa and tempb):
        errhandler.storeError("Either variables are empty: A = " + tempa + ", B = " + tempb)

if not errhandler.failed:
    size = (int(multiplier*int(tempa)), int(multiplier*int(tempb)))

    pygame.init()
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    while errhandler.failed == False:
        elapsed = (datetime.datetime.now() - start).total_seconds()
        mb = pygame.mouse.get_pressed()
        mp = pygame.mouse.get_pos()
        c = int(50 + (2*sin(elapsed)))
        window.fill((c,c,c))
        oscommands.clearConsole()
        print(elapsed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                errhandler.storeError("App terminate request")

        pygame.display.flip()
        clock.tick()

print(errhandler.tellErrors())
pygame.quit()