from libraries import overground
import pygame

overground.oscommands.clearConsole()

canvasmult = (50,50)

clock = pygame.time.Clock()

temp = ""

startBool = True
while startBool:
    temp = ""
    size = input("Insert the width and height of the word search:\n(read as W,H)\n")
    for i in range(len(size)):
        if size[i] in "0123456789,":
            temp += size[i]
    size = temp.split(",")
    if len(size) == 2:
        try:
            size[0] = int(size[0])
            size[1] = int(size[1])
            startBool = False
        except:
            pass
startBool = True
while startBool:
    characters = input("Insert the characters of the word search:\n(from left to right, top row to bottom row)\n")
    if len(characters) != size[0] * size[1]:
        print("The number of characters does not match the size of the word search.")
    else:
        startBool = False
startBool = True
while startBool:
    words = input("Insert the words to be found (separated by commas):\n")
    temp = ""
    for i in range(len(words)):
        if words[i].lower() in "abcdefghijklmnopqrstuvwxyz,":
            temp += words[i]
    words = temp
    try:
        words = words.split(",")
        startBool = False
    except:
        pass
charlist = []
for i in range(size[1]):
    temp = ""
    for j in range(size[0]):
        temp += characters[j+(i*size[1])]
    charlist.append(temp)


pygame.init()
screen = pygame.display.set_mode((size[0] * canvasmult[0], size[1] * canvasmult[1]))

startPositions = []
endPositions = []

print(characters,"\n",charlist,"\n",words)

for i in range(size[1]):
    for j in range(size[0]):
        for k in range(len(words)):
            tempa = ""
            tempb = []
            temp = ""
            tempr = ""
            temprd= ""
            tempd = ""
            templd= ""
            templ = ""
            templu= ""
            tempu = ""
            tempru= ""
            if words[k][0] == charlist[i][j]:
                tempa = (j * canvasmult[0] + 25,i * canvasmult[1] + 25)
                for l in range(len(words[k])-1):
                    try:
                        if charlist[i][j+l+1] == words[k][l+1]:
                            tempr+=charlist[i][j+l+1]
                    except: pass
                    try:
                        if charlist[i+l+1][j+l+1] == words[k][l+1]:
                            temprd+=charlist[i+l+1][j+l+1]
                    except: pass
                    try:
                        if charlist[i+l+1][j] == words[k][l+1]:
                            tempd+=charlist[i+l+1][j]
                    except: pass
                    try:
                        if charlist[i+l+1][j-l-1] == words[k][l+1]:
                            templd+=charlist[i+l+1][j-l-1]
                    except: pass
                    try:
                        if charlist[i][j-l-1] == words[k][l+1]:
                            templ+=charlist[i][j-l-1]
                    except: pass
                    try:
                        if charlist[i-l-1][j-l-1] == words[k][l+1]:
                            templu+=charlist[i-l-1][j-l-1]
                    except: pass
                    try:
                        if charlist[i-l-1][j] == words[k][l+1]:
                            tempu+=charlist[i-l-1][j]
                    except: pass
                    try:
                        if charlist[i-l-1][j+l+1] == words[k][l+1]:
                            tempru+=charlist[i-l-1][j+l+1]
                    except: pass
                find = []
                temp = words[k][0] + tempr
                if temp == words[k]:
                    tempb.append((j+len(words[k])-1,i))
                    find.append("right")
                temp = words[k][0] + temprd
                if temp == words[k]:
                    tempb.append((j+len(words[k])-1,i+len(words[k])-1))
                    find.append("diagonally down-right")
                temp = words[k][0] + tempd
                if temp == words[k]:
                    tempb.append((j,i+len(words[k])-1))
                    find.append("down")
                temp = words[k][0] + templd
                if temp == words[k]:
                    tempb.append((j-len(words[k])+1,i+len(words[k])-1))
                    find.append("diagonally down-left")
                temp = words[k][0] + templ
                if temp == words[k]:
                    tempb.append((j-len(words[k])+1,i))
                    find.append("left")
                temp = words[k][0] + templu
                if temp == words[k]:
                    tempb.append((j-len(words[k])-1,i-len(words[k])-1))
                    find.append("diagonally up-left")
                temp = words[k][0] + tempu
                if temp == words[k]:
                    tempb.append((j,i-len(words[k])+1))
                    find.append("up")
                temp = words[k][0] + tempru
                if temp == words[k]:
                    tempb.append((j+len(words[k])-1,i-len(words[k])-1))
                    find.append("diagonally up-right")
                for h in range(len(tempb)):
                    temph = (tempb[h][0] * canvasmult[0] + 25,tempb[h][1] * canvasmult[1] + 25)
                    startPositions.append(tempa)
                    endPositions.append(temph)
                    final = ""
                    if len(find) == 1:
                        final = find[0]
                    elif len(find) == 2:
                        final = find[0] + " and " + find[1]
                    else:
                        for i in range(len(find)):
                            if i == 0:
                                final += find[0]
                            else:
                                final += "and " + find[i]
                    print("Found '" + words[k] + "' going " + final)

lmbd = False
selected = []
tempselect = []
for i in range(len(characters)):
    selected.append(0)
    tempselect.append(0)
font = pygame.font.SysFont("Menlo", int(((canvasmult[0] + canvasmult[1])/2)*0.4))

while True:
    clock.tick(60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                lmbd = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                tempselect = selected[:]
                lmbd = False
    
    if lmbd:
        tempos = pygame.mouse.get_pos()
        pos = int((tempos[0]/screen.get_width())*size[0])+(int((tempos[1]/screen.get_height())*size[1])*size[1])
        if selected[i] == tempselect[i]:
            if tempselect[pos] == 1:
                selected[pos] = 0
            else:
                selected[pos] = 1
    screen.fill((0,0,0))
    for i in range(len(selected)):
        if selected[i] == 1:
            temp = pygame.Rect(((i%size[0])*canvasmult[0])+(canvasmult[0]/8),(int(i/size[1])*canvasmult[1])+(canvasmult[1]/8),canvasmult[0]-(canvasmult[0]/4),canvasmult[1]-(canvasmult[1]/4))
            pygame.draw.rect(screen,(50,50,50),temp)
    for i in range(len(startPositions)):
        pygame.draw.line(screen, (127,127,0), startPositions[i], endPositions[i], 16)
    for i in range(len(startPositions)):
        pygame.draw.circle(screen,(127,0,0),startPositions[i],16)
    for i in range(len(startPositions)):
        pygame.draw.circle(screen,(0,0,0),startPositions[i],8)
    for i in range(len(startPositions)):
        pygame.draw.circle(screen,(0,127,0),endPositions[i],10)
    for i in range(len(selected)):
        if selected[i] == 1:
            temp = pygame.Rect(((i%size[0])*canvasmult[0])+(canvasmult[0]/8),(int(i/size[1])*canvasmult[1])+(canvasmult[1]/8),canvasmult[0]-(canvasmult[0]/4),canvasmult[1]-(canvasmult[1]/4))
            pygame.draw.lines(screen,(255,255,255),False,[temp.topleft,temp.topright,temp.bottomright,temp.bottomleft,temp.topleft])
    for i in range(size[1]):
        for j in range(size[0]):
            x = j * canvasmult[0] + 19
            y = i * canvasmult[1] + 14
            text = font.render(charlist[i][j].upper(), True, (255, 255, 255))
            screen.blit(text, (x, y))
    pygame.display.flip()