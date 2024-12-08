import os
import pygame
from pygame.locals import *
import pygame.font

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole()

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Tennis Counter")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
clock = pygame.time.Clock()
isquit = False

class buttons:
    settingsprivate = pygame.image.load("assets/settings.png")
    settingsprivate.convert()
    settingsrect = settingsprivate.get_rect()
    settingsrect.x = 40
    settingsrect.y = 40

while isquit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isquit = True
    window.fill((90,90,90))

    temp = pygame.transform.rotozoom(buttons.settings, 0, 1)

    window.blit(buttons.settings,buttons.settingsrect)
    pygame.display.flip()
    clock.tick(60)
pygame.font.quit()
pygame.quit()