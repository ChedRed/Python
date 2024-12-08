from tkinter import filedialog, Tk

import pygame
from PIL import Image

screenmult = 3

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def openFile():
    root = Tk()
    root.withdraw()
    f = filedialog.askopenfilename(defaultextension=".png",filetypes=[("PNG Images", "*.png"), ("JPEG Images", "*.jpg")])
    root.destroy()
    return f

def saveFile():
    root = Tk()
    root.withdraw()
    f = filedialog.asksaveasfilename(initialdir=tout,defaultextension=".png",filetypes=[("PNG Images", "*.png"), ("JPEG Images", "*.jpg")])
    root.destroy()
    return f

file = openFile()
if file: img = [None,None,None,None,Image.open(file),None,None,None,None]
else: exit()

pygame.init()
screen = pygame.display.set_mode((img[4].width * screenmult, img[4].height * screenmult))
clock = pygame.time.Clock()

pgimg = [None,None,None,None,pygame.transform.scale_by(pygame.image.load(file), screenmult),None,None,None,None]

width = min(img[4].width,img[4].height) * screenmult

pygame.display.set_caption("Texture Browser")

scale = 1
borders = [0,0,0,0]
tilescale = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
running = True
tout = None
rightMouse = False
rightagain = False
while running:
    mouseaction = False
    rightagain = False
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEWHEEL:
            scale += clamp(event.y, -5, 5)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseaction = True
            elif event.button == 3:
                rightMouse = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                rightMouse = False
                rightagain = True
                # tfile = openFile()
                # if tfile:
                #     img = Image.open(tfile)
                #     pgimg = pygame.transform.scale_by(pygame.image.load(tfile), screenmult)
                    # screen = pygame.display.set_mode((img[4].width * screenmult, img[4].height * screenmult))

    screen.fill((0,0,0))
    scale = clamp(scale,0,4)

    recte = (round((x-((int((width/screenmult)/pow(2,scale))/2)*screenmult))/(int((width/screenmult)/pow(2,scale))*screenmult))*(int((width/screenmult)/pow(2,scale))*screenmult),round((y-((int((width/screenmult)/pow(2,scale))/2)*screenmult))/(int((width/screenmult)/pow(2,scale))*screenmult))*(int((width/screenmult)/pow(2,scale))*screenmult),int((width/screenmult)/pow(2,scale))*screenmult,int((width/screenmult)/pow(2,scale))*screenmult)
    pygame.draw.rect(screen,(127,127,127),recte)
    for i in range(len(pgimg)):
        if pgimg[i]:
            screen.blit(pgimg[i], (0,0))

    if rightMouse:
        if pgimg[4]:
            if x<img[4].width*screenmult/3:
                if y<img[4].height*screenmult/3:
                    pygame.draw.rect(screen,(0,255,0),(0,0,img[4].width*screenmult/3,img[4].height*screenmult/3))
                elif y>img[4].height*screenmult/3 and y<2*(img[4].height*screenmult/3):
                    pygame.draw.rect(screen,(0,255,0),(0,img[4].height*screenmult/3,img[4].width*screenmult/3,img[4].height*screenmult/3))
                elif y>2*(img[4].height*screenmult/3):
                    pygame.draw.rect(screen,(0,255,0),(0,2*(img[4].height*screenmult/3),img[4].width*screenmult/3,img[4].height*screenmult/3))
            elif x>img[4].width*screenmult/3 and x<2*(img[4].width*screenmult/3):
                if y<img[4].height*screenmult/3:
                    pygame.draw.rect(screen,(0,255,0),(img[4].width*screenmult/3,0,img[4].width*screenmult/3,img[4].height*screenmult/3))
                elif y>img[4].height*screenmult/3 and y<2*(img[4].height*screenmult/3):
                    pygame.draw.rect(screen,(0,255,0),(img[4].width*screenmult/3,img[4].height*screenmult/3,img[4].width*screenmult/3,img[4].height*screenmult/3))
                elif y>2*(img[4].height*screenmult/3):
                    pygame.draw.rect(screen,(0,255,0),(img[4].width*screenmult/3,2*(img[4].height*screenmult/3),img[4].width*screenmult/3,img[4].height*screenmult/3))
            elif x>2*(img[4].width*screenmult/3):
                if y<img[4].height*screenmult/3:
                    pygame.draw.rect(screen,(0,255,0),(2*(img[4].width*screenmult/3),0,img[4].width*screenmult/3,img[4].height*screenmult/3))
                elif y>img[4].height*screenmult/3 and y<2*(img[4].height*screenmult/3):
                    pygame.draw.rect(screen,(0,255,0),(2*(img[4].width*screenmult/3),img[4].height*screenmult/3,img[4].width*screenmult/3,img[4].height*screenmult/3))
                elif y>2*(img[4].height*screenmult/3):
                    pygame.draw.rect(screen,(0,255,0),(2*(img[4].width*screenmult/3),2*(img[4].height*screenmult/3),img[4].width*screenmult/3,img[4].height*screenmult/3))
    if rightagain:
        newpos = 0
        if x<img[4].width*screenmult/3:
            if y<img[4].height*screenmult/3:
                newpos = 1
                borders[0]=1
                borders[1]=1
            elif y>img[4].height*screenmult/3 and y<2*(img[4].height*screenmult/3):
                newpos = 4
                borders[1]=1
            elif y>2*(img[4].height*screenmult/3):
                newpos = 7
                borders[1]=1
                borders[2]=1
        elif x>img[4].width*screenmult/3 and x<2*(img[4].width*screenmult/3):
            if y<img[4].height*screenmult/3:
                newpos = 2
                borders[0]=1
            elif y>img[4].height*screenmult/3 and y<2*(img[4].height*screenmult/3):
                newpos = 5
            elif y>2*(img[4].height*screenmult/3):
                newpos = 8
                borders[2]=1
        elif x>2*(img[4].width*screenmult/3):
            if y<img[4].height*screenmult/3:
                newpos = 3
                borders[0]=1
                borders[3]=1
            elif y>img[4].height*screenmult/3 and y<2*(img[4].height*screenmult/3):
                newpos = 6
                borders[3]=1
            elif y>2*(img[4].height*screenmult/3):
                newpos = 9
                borders[2]=1
                borders[3]=1
        newfile = openFile()
        print(newpos)
        if newfile:
            img[newpos-1] = Image.open(newfile)
            pgimg[newpos-1] = pygame.transform.scale_by(pygame.image.load(newfile), screenmult)
        newscale = [0,0]
        for i in range(len(img)):
            if img[i]:
                if i==0:
                    newscale[0] += img[i].width
                    newscale[1] += img[i].height
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
                elif i==1:
                    newscale[1] += img[i].height
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
                elif i==2:
                    newscale[0] += img[i].width
                    newscale[1] += img[i].height
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
                elif i==3:
                    newscale[0] += img[i].width
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
                elif i==4:
                    newscale[0] += img[i].width
                    newscale[1] += img[i].height
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
                elif i==5:
                    newscale[0] += img[i].width
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
                elif i==6:
                    newscale[0] += img[i].width
                    newscale[1] += img[i].height
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
                elif i==7:
                    newscale[1] += img[i].height
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
                elif i==8:
                    newscale[0] += img[i].width
                    newscale[1] += img[i].height
                    tilescale[i].x += img[i].width
                    tilescale[i].y += img[i].height
        print(newscale)
        pygame.display.set_mode((newscale[0]*screenmult,newscale[1]*screenmult))
    if mouseaction:
        out = saveFile()
        if out:
            tout = out
            img.crop((recte[0]/screenmult,recte[1]/screenmult,(recte[0]/screenmult)+(recte[2]/screenmult),(recte[1]/screenmult)+(recte[3]/screenmult))).save(out)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()