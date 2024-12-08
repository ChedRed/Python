from libraries import overground
import pygame


ogcommands = overground.oscommands

ogcommands.clearConsole()

ogredefine = overground.redefinition

canvasmult = (25,25)

bordermult = (1.05,1.05)

clock = pygame.time.Clock()

temp = ""

size = "10,6"

characters = ""

tempwords = "west,mountain,oregon,trail,cotton,wood,iron,land,frontier,wagon"

# Input the number of cells widthwise and heightwise.
while True:
    if size == "":
        size = input("Insert the width and height of the word search:\n(read as W,H)\n")
    else:
        print("size = " + size)
    temp = ogredefine.filter(size,"01234657890,")
    size = temp.split(",")
    if len(size) == 2:
        try:
            size[0] = int(size[0])
            size[1] = int(size[1])
            break
        except:
            pass

# Input the characters to fill the grid.
while True:
    if characters == "":
        characters = input("Insert the characters of the word search:\n(from left to right, top row to bottom row)\n(You can also enter nothing to make your own!)\n")
    else:
        print("characters = " + characters)
    if len(characters) != size[0] * size[1]:
        if len(characters) != 0:
            print("The number of characters does not match the size of the word search.")
        else:
            characters = " " * (size[0] * size[1])
            break
    else:
        break

# Input a list containing the words to search for.
words = []
while True:
    endimmediately = False
    if tempwords == "":
        tempwords = input("Insert the words to be found (separated by commas) or type '$END' to finish word list:\n")
    else:
        endimmediately = True
        print("words = " + str(tempwords))
    if tempwords == "$END":
        print(words)
        break
    if "$END" in tempwords:
        tempwords.replace("$END","")
        endimmediately = True
    tempwords = ogredefine.filter(tempwords, "abcdefghijklmnopqrstuvwxyz,")

    try:
        tempwords = tempwords.split(",")
        words += tempwords
    except Exception as e:
        print(e)
        endimmediately = False
    if endimmediately:
        break

charlist = []

for i in range(size[1]):
    temp = ""
    for j in range(size[0]):
        temp += characters[j+(i*size[1])]
    charlist.append(temp)

findwords = words[:]

startPositions = []
endPositions = []

foundwordata = []
dupewords = []

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
                tempa = (j * canvasmult[0] + (canvasmult[0]/2),i * canvasmult[1] + (canvasmult[1]/2))
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
                    tempb.append((j-len(words[k])+1,i-len(words[k])+1))
                    find.append("diagonally up-left")
                temp = words[k][0] + tempu
                if temp == words[k]:
                    tempb.append((j,i-len(words[k])+1))
                    find.append("up")
                temp = words[k][0] + tempru
                if temp == words[k]:
                    tempb.append((j+len(words[k])-1,i-len(words[k])+1))
                    find.append("diagonally up-right")
                for h in range(len(tempb)):
                    temph = (tempb[h][0] * canvasmult[0] + (canvasmult[0]/2),tempb[h][1] * canvasmult[1] + (canvasmult[1]/2))
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
                    if words[k] in findwords:
                        findwords.remove(words[k])
                    else:
                        dupewords.append(words[k])

# List missing words.
print("\nMissing " + str(len(findwords)) + " words.")
temp = ogredefine.listToString(findwords, ", ")
if temp == "":
    print("")
else:
    print(temp + "\n")

#list duplicates.
print(str(len(dupewords)) + " duplicate words found.")

print(ogredefine.listToString(dupewords, ", "))

# Scan again and remove duplicates.

# Create pygame interface.
pygame.init()
screen = pygame.display.set_mode(((size[0]*bordermult[0]) * canvasmult[0], (size[1]*bordermult[1]) * canvasmult[1]))
pygame.display.set_caption("Word Search Solver","WSS")

screensize = [size[0]*canvasmult[0],size[1]*canvasmult[1]]
lmbd = False
selected = []
tempselect = []
for i in range(len(characters)):
    selected.append(0)
    tempselect.append(0)
font = pygame.font.SysFont("Menlo", int(((canvasmult[0] + canvasmult[1])/2)*0.4))

offset = ((screen.get_width() - screensize[0])/2,(screen.get_height() - screensize[1])/2)

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
        tempos = (tempos[0]-offset[0],tempos[1]-offset[1])
        pos = int((tempos[0]/screensize[0])*size[0])+(int((tempos[1]/screensize[1])*size[1])*size[1])
        try:
            if selected[i] == tempselect[i]:
                if tempselect[pos] == 1:
                    selected[pos] = 0
                else:
                    selected[pos] = 1
        except: pass
    screen.fill((0,0,0))
    for i in range(len(selected)):
        if selected[i] == 1:
            temp = pygame.Rect(((i%size[0])*canvasmult[0])+(canvasmult[0]/8)+offset[0],(int(i/size[1])*canvasmult[1])+(canvasmult[1]/8)+offset[1],canvasmult[0]-(canvasmult[0]/4),canvasmult[1]-(canvasmult[1]/4))
            pygame.draw.rect(screen,(50,50,50),temp)
    for i in range(len(startPositions)):
        pygame.draw.line(screen, (127,127,0), (startPositions[i][0]+offset[0],startPositions[i][1]+offset[1]), (endPositions[i][0]+offset[0],endPositions[i][1]+offset[1]), 16)
    for i in range(len(startPositions)):
        pygame.draw.circle(screen,(127,0,0),(startPositions[i][0]+offset[0],startPositions[i][1]+offset[1]),16)
    for i in range(len(startPositions)):
        pygame.draw.circle(screen,(0,0,0),(startPositions[i][0]+offset[0],startPositions[i][1]+offset[1]),8)
    for i in range(len(startPositions)):
        pygame.draw.circle(screen,(0,127,0),(endPositions[i][0]+offset[0],endPositions[i][1]+offset[1]),10)
    for i in range(len(selected)):
        if selected[i] == 1:
            temp = pygame.Rect(((i%size[0])*canvasmult[0])+(canvasmult[0]/8)+offset[0],(int(i/size[1])*canvasmult[1])+(canvasmult[1]/8)+offset[1],canvasmult[0]-(canvasmult[0]/4),canvasmult[1]-(canvasmult[1]/4))
            pygame.draw.lines(screen,(255,255,255),False,[temp.topleft,temp.topright,temp.bottomright,temp.bottomleft,temp.topleft])
    for i in range(size[1]):
        for j in range(size[0]):
            x = j * canvasmult[0] + ((canvasmult[0]/2)-(6*(canvasmult[0]/50)))+offset[0]
            y = i * canvasmult[1] + ((canvasmult[1]/2)-(12*(canvasmult[1]/50)))+offset[1]
            text = font.render(charlist[i][j].upper(), True, (255, 255, 255))
            screen.blit(text, (x, y))
    pygame.display.flip()