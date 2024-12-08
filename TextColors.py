#Setup
import os
from PIL import Image, ImageDraw
import pygame

i = 255

pygame.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption("PIMP - Python Image Manipulation Tool v1.0")
screen.fill((127, 127, 127))
os.chdir("/Users/ryanchou/Desktop")
path = "/Users/ryanchou/Desktop"
ImFolder = path + "/"

#Variables
width = 256
height = 256
r, g, b = 255, 0, 0
images = []

rIm = Image.new('RGBA', (width, height), color=(0,0,0,0))

#Loop
running = True
pygame.display.update()
while running:
    screen.fill((127, 127, 127))
    if i > 0:
        if r >= 255:
            r = 0
        else:
            r += 1
        im = Image.new('RGBA', (width, height), color=(0,0,0,0))
        draw = ImageDraw.Draw(im)
        draw.rectangle((0, 0, width, height), fill=(r, g, b))
        images.append(im)
        pygame.draw.rect(screen, (r, g, b), (0, 0, width, height))
    pygame.display.update()
    #End
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    i -= 1
pygame.quit()

images[0].save('Desktop/PIMP output.png', save_all = True, append_images = images[1:])