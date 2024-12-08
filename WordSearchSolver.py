# Imports
import math
import os
from libraries import overground
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# Definitions
clock = pygame.time.Clock()
ogredefine = overground.redefinition
ssize = [900,900]
sizemult = []
chargrid = []
gridata = []
wordlist = []
wordindex = []

# Setup variables
size = "30,30"
charstring = "radiumrliinhretmslsantimonyrilelurziumavohneeceoicyiereppocuuirmetbitwtinncnaedthittumatimnmulekcinuriddhmbdtitrsrruflusgrbtmmtamodeyinooemnugocobaltcmuimuuosuolsnoeerreinmompgrdraoudaiailiepodctbgrauutmuilebonmcigcbfrvrrapmimiotmnmhmuurnkdtaunnsmioirrruuuumrbhipommmeiillmeanuscmmmmimimiedgnlrrubgiuiiesrmibsrrunsrhlrnsybuuiimimmtfiifurtonseiuttklnolhtvvburuehonumiaemhgmvmeesdydchoaarhmieiromhdmngtrpailmuibrerntneolsnunnutrannmuinilodagnenitatsasgmimimoseiucsuourhnilabuzddanabluucufossntmmmrplufcsrmiimplhrbmiiirosneodymiummeinluguulyuonumnceriidneptuniumnatimmialmmehyrihuncbmanamiciieirtpudtutiuidertielyiugumldncsprnmiiiiondeopeucmaluminumyaurssomlrnymeureomrtanossenagotlaiarluiubcmerscaenmtmiueiemuillahtchimeudlmaphosphoruscblmtvcaesotcdlldmercurytaargonaaeemfdpnnpdroxoeapoxygenotpyrkrrsnmuiclacgehxavnyttriumuidniobiumuinehrnnirceriumuimrefmlieuoumsiliconinccesiumuilehimuimsonmboronhmszs"
wordstring = "actinium, aluminum, americium, antimony, argon, arsenic, astatine, barium, berkelium, beryllium, bismuth, bohrium, boron, bromine, cadmium, calcium, californium, carbon, cerium, cesium, chlorine, chromium, cobalt, copernicium, copper, curium, darmstadtium, dubnium, dysprosium, einsteinium, erbium, europium, fermium, flerovium, fluorine, francium, gadolinium, gallium, germanium, gold, hafnium, hassium, helium, holmium, hydrogen, indium, iodine, iridium, iron, krypton, lanthanum, lawrencium, lead, lithium, livermorium, lutetium, magnesium, manganese, meitnerium, mendelevium, mercury, molybdenum, moscovium, neodymium, neon, neptunium, nickel, nihonium, niobium, nitrogen, nobelium, oganesson, osmium, oxygen, palladium, phosphorus, platinum, plutonium, polonium, potassium, praseodymium, promethium, protactinium, radium, radon, rhenium, rhodium, roentgenium, rubidium, ruthenium, rutherfordium, samarium, scandium, seaborgium, selenium, silicon, silver, sodium, strontium, sulfur, tantalum, technetium, tennessine, terbium, thallium, thorium, thulium, tin, titanium, tungsten, uranium, vanadium, xenon, ytterbium, yttrium, zinc, zirconium $end"



# Define the size if not already defined.
while True:
    if size == "":
        size = input("Insert the size of the word search (Width x Height): ")
    else:
        print("Size = " + size)
    size = ogredefine.filter(size.lower(),"1234567890,x")
    try: # Get dimensions method 1 [Width, Height]
        size = size.split(",")
        size = (int(size[0]),int(size[1]))
        break
    except: # Get dimensions method 2 [Width x Height]
        try:
            size = size.split("x")
            size = (int(size[0]),int(size[1]))
            break
        except: # On fail, reset size.
            print("The size was not defined correctly.")
            size = ""

# Define the characters if not already defined.
while True:
    if charstring == "":
        charstring = input("Insert the characters in the word search from left to right, top to bottom.\n")
    else:
        print("Characters = " + charstring)
    charstring = ogredefine.filter(charstring.lower(),"abcdefghijklmnopqrstuvwxyz")
    if len(charstring) == size[0] * size[1]:
        for y in range(size[1]):
            temp = ""
            for x in range(size[0]):
                temp += charstring[(y*size[0]+x)]
            chargrid.append(temp)
        break
    else:
        print("The character string does not have the correct size for this " + str(size[0]) + " by " + str(size[1]) + " size word search.")
        charstring = ""

# Define the words if not already defined.
while True:
    if wordstring == "":
        wordstring = input("List out the words you have, separated by commas. Type '$end' to stop listing.\n")
    else:
        print("Words = " + wordstring)
    wordstring = ogredefine.filter(wordstring.lower(),"abcdefghijklmnopqrstuvwxyz,$")
    if "$end" == wordstring:
        break
    if "$end" in wordstring:
        wordstring = wordstring.replace("$end","")
        wordstring = wordstring.split(",")
        for i in range(len(wordstring)):
            wordlist.append(wordstring[i].lower())
        break
    else:
        wordstring = wordstring.split(",")
        for i in range(len(wordstring)):
            wordlist.append(wordstring[i].lower())

for i in range(len(wordlist)):
    wordindex.append((wordlist[i],[],[],[])) # Word, starting coordinates list, ending coordinates list, directions list.



# -- Current variables:
# size; width and height (number of spaces) in word search.
# chargrid; character at each space (y,x) in word search.
# wordlist; words to search for.
# wordindex; information for each word (start and end positions, directions for those positions).

# Begin word indexing.
for y in range(size[1]):
    for x in range(size[0]):
        for w in range(len(wordlist)):
            if wordlist[w][0] == chargrid[y][x]:
                # dirlen is temporary, used to find which directions the word is found on a starting tile.
                dirlen = [1,1,1,1,1,1,1,1] # right, down-right, down, down-left, left, up-left, up, up-right
                for l in range(len(wordlist[w])-1):
                    try:
                        if chargrid[y][x+l+1] == wordlist[w][l+1]: dirlen[0] += 1
                    except: pass
                    try:
                        if chargrid[y+l+1][x+l+1] == wordlist[w][l+1]: dirlen[1] += 1
                    except: pass
                    try:
                        if chargrid[y+l+1][x] == wordlist[w][l+1]: dirlen[2] += 1
                    except: pass
                    try:
                        if chargrid[y+l+1][x-l-1] == wordlist[w][l+1]: dirlen[3] += 1
                    except: pass
                    try:
                        if chargrid[y][x-l-1] == wordlist[w][l+1]: dirlen[4] += 1
                    except: pass
                    try:
                        if chargrid[y-l-1][x-l-1] == wordlist[w][l+1]: dirlen[5] += 1
                    except: pass
                    try:
                        if chargrid[y-l-1][x] == wordlist[w][l+1]: dirlen[6] += 1
                    except: pass
                    try:
                        if chargrid[y-l-1][x+l+1] == wordlist[w][l+1]: dirlen[7] += 1
                    except: pass

                wordir = []
                wordlen = len(wordlist[w])
                # right, down-right, down, down-left, left, up-left, up, up-right
                temp = []
                if dirlen[0] == wordlen:
                    wordir.append("right")
                    temp.append((x+wordlen-1,y))
                if dirlen[1] == wordlen:
                    wordir.append("diagonally down-right")
                    temp.append((x+wordlen-1,y+wordlen-1))
                if dirlen[2] == wordlen:
                    wordir.append("down")
                    temp.append((x,y+wordlen-1))
                if dirlen[3] == wordlen:
                    wordir.append("diagonally down-left")
                    temp.append((x-wordlen+1,y+wordlen-1))
                if dirlen[4] == wordlen:
                    wordir.append("left")
                    temp.append((x-wordlen+1,y))
                if dirlen[5] == wordlen:
                    wordir.append("diagonally up-left")
                    temp.append((x-wordlen+1,y-wordlen+1))
                if dirlen[6] == wordlen:
                    wordir.append("up")
                    temp.append((x,y-wordlen+1))
                if dirlen[7] == wordlen:
                    wordir.append("diagonally up-right")
                    temp.append((x+wordlen-1,y-wordlen+1))

                if len(wordir) > 0:
                    wordindex[w][1].append((x, y))
                    wordindex[w][2].append(temp)
                temp = "Found word '" + wordlist[w] + "' going "
                for i in range(len(wordir)):
                    wordindex[w][3].append(wordir[i])
                    if i == 0:
                        temp += wordir[i]
                    if len(wordir) >= 2:
                        if i == len(wordir):
                            temp += ", and " + wordir[i]
                        else:
                            temp += ", " + wordir[i]
                    elif i != 0:
                        temp += " and " + wordir[i]
                if len(wordir) > 0:
                    print(temp + ".")

print(wordindex)

# Start pygame

pygame.init()

screen = pygame.display.set_mode(ssize,pygame.RESIZABLE)
sizemult = [ssize[0]/size[0],ssize[1]/size[1]]
font = pygame.font.SysFont("Menlo",int((sizemult[0]+sizemult[1])/2))
fsize = font.size("Menlo")
transurface = pygame.Surface((ssize[0], ssize[1]), pygame.SRCALPHA)
temptransurface = pygame.Surface((ssize[0], ssize[1]), pygame.SRCALPHA)
transurface.fill((0, 0, 0, 0))

while True:
    # Definitions and updates
    screen.fill((0,0,0))
    clock.tick(60)
    transurface.fill((0, 0, 0, 0))
    temptransurface.fill((0, 0, 0, 0))
    if ssize != pygame.display.get_surface().get_size():
        ssize = pygame.display.get_surface().get_size()
        sizemult = [ssize[0]/size[0],ssize[1]/size[1]]
        font = pygame.font.SysFont("Menlo",int(min(sizemult[0],sizemult[1])))
        transurface = pygame.Surface((ssize[0], ssize[1]), pygame.SRCALPHA)
        temptransurface = pygame.Surface((ssize[0], ssize[1]), pygame.SRCALPHA)

    # Event handling
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

    # Prepare lines
    for w in range(len(wordindex)):
        for s in range(len(wordindex[w][1])):
            for e in range(len(wordindex[w][2][s])):
                pygame.draw.line(temptransurface,(255,255,255,75),((int(wordindex[w][1][s][0]*sizemult[0]+(sizemult[0]/2)),int(wordindex[w][1][s][1]*sizemult[1]+(sizemult[1]/2)))),(int(wordindex[w][2][s][e][0]*sizemult[0]+(sizemult[0]/2)),int(wordindex[w][2][s][e][1]*sizemult[1]+(sizemult[1]/2))),int(int(min(sizemult[0],sizemult[1]))/2))
                transurface.blit(temptransurface, (0, 0))
                temptransurface.fill((0, 0, 0, 0))
    # Draw start points
    for w in range(len(wordindex)):
        for s in range(len(wordindex[w][1])):
            rotation = 0
            if wordindex[w][3][s] == 'up': rotation = 4
            if wordindex[w][3][s] == 'diagonally up-right': rotation = 3
            if wordindex[w][3][s] == 'right': rotation = 2
            if wordindex[w][3][s]  == 'diagonally down-right': rotation = 1
            if wordindex[w][3][s] == 'down': rotation = 0
            if wordindex[w][3][s] == 'diagonally down-left': rotation = 7
            if wordindex[w][3][s] == 'left': rotation = 6
            if wordindex[w][3][s] == 'diagonally up-left': rotation = 5
            base = (int(wordindex[w][1][s][0]*sizemult[0])+(sizemult[0]/2),int(wordindex[w][1][s][1]*sizemult[1])+(sizemult[1]/2))
            pygame.draw.polygon(temptransurface,(100,100,200,200),[(base[0]+(math.sin(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),base[1]+math.cos(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),(base[0]+(math.sin(math.pi*(rotation+5)*45/180)*int(min(sizemult[0],sizemult[1]))),base[1]+math.cos(math.pi*(rotation+5)*45/180)*int(min(sizemult[0],sizemult[1]))),(base[0]+(math.sin(math.pi*rotation*45/180)*int(min(sizemult[0],sizemult[1]))),base[1]+math.cos(math.pi*rotation*45/180)*int(min(sizemult[0],sizemult[1]))),(base[0]+(math.sin(math.pi*(rotation+3)*45/180)*int(min(sizemult[0],sizemult[1]))),base[1]+math.cos(math.pi*(rotation+3)*45/180)*int(min(sizemult[0],sizemult[1])))])
            pygame.draw.polygon(temptransurface,(0,0,0),[(base[0]+(math.sin(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/4)),base[1]+math.cos(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/4)),(base[0]+(math.sin(math.pi*(rotation+5)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),base[1]+math.cos(math.pi*(rotation+5)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),(base[0]+(math.sin(math.pi*rotation*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),base[1]+math.cos(math.pi*rotation*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),(base[0]+(math.sin(math.pi*(rotation+3)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),base[1]+math.cos(math.pi*(rotation+3)*45/180)*(int(min(sizemult[0],sizemult[1]))/2))])
            transurface.blit(temptransurface, (0, 0))
            temptransurface.fill((0, 0, 0, 0))
    # Blit transparent objects
    screen.blit(transurface, (0, 0))
    # Draw end points
    for w in range(len(wordindex)):
        for s in range(len(wordindex[w][1])):
            for e in range(len(wordindex[w][2][s])):
                rotation = 0
                if wordindex[w][3][s] == 'up': rotation = 0
                if wordindex[w][3][s] == 'diagonally up-right': rotation = 7
                if wordindex[w][3][s] == 'right': rotation = 6
                if wordindex[w][3][s]  == 'diagonally down-right': rotation = 5
                if wordindex[w][3][s] == 'down': rotation = 4
                if wordindex[w][3][s] == 'diagonally down-left': rotation = 3
                if wordindex[w][3][s] == 'left': rotation = 2
                if wordindex[w][3][s] == 'diagonally up-left': rotation = 1
                #pygame.draw.rect(screen,(200,100,0),((int(wordindex[w][2][s][e][0]*sizemult[0])+1,int(wordindex[w][2][s][e][1]*sizemult[1])+1),(sizemult[0],sizemult[1])),0,0)
                base = (int(int(wordindex[w][2][s][e][0]*sizemult[0])+(sizemult[0]/2)-math.sin(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),int(int(wordindex[w][2][s][e][1]*sizemult[1])+(sizemult[1]/2)-math.cos(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)))
                pygame.draw.polygon(screen,(200,100,0),[(base[0]+(math.sin(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),base[1]+math.cos(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),(base[0]+(math.sin(math.pi*(rotation+5)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),base[1]+math.cos(math.pi*(rotation+5)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),(base[0]+(math.sin(math.pi*rotation*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),base[1]+math.cos(math.pi*rotation*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),(base[0]+(math.sin(math.pi*(rotation+3)*45/180)*(int(min(sizemult[0],sizemult[1]))/2)),base[1]+math.cos(math.pi*(rotation+3)*45/180)*(int(min(sizemult[0],sizemult[1]))/2))])
                pygame.draw.polygon(screen,(200,150,75),[(base[0]+(math.sin(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/2-5)),base[1]+math.cos(math.pi*(rotation+4)*45/180)*(int(min(sizemult[0],sizemult[1]))/2-5)),(base[0]+(math.sin(math.pi*(rotation+5)*45/180)*(int(min(sizemult[0],sizemult[1]))/2-5)),base[1]+math.cos(math.pi*(rotation+5)*45/180)*(int(min(sizemult[0],sizemult[1]))/2-5)),(base[0]+(math.sin(math.pi*rotation*45/180)*(int(min(sizemult[0],sizemult[1]))/2-5)),base[1]+math.cos(math.pi*rotation*45/180)*(int(min(sizemult[0],sizemult[1]))/2-5)),(base[0]+(math.sin(math.pi*(rotation+3)*45/180)*(int(min(sizemult[0],sizemult[1]))/2-5)),base[1]+math.cos(math.pi*(rotation+3)*45/180)*(int(min(sizemult[0],sizemult[1]))/2-5))])
    for y in range(size[1]):
        for x in range(size[0]):
            text = font.render(chargrid[y][x], True, (255, 255, 255))
            screen.blit(text,(sizemult[0]*x+(sizemult[0]/2)-(text.get_width()/2),sizemult[1]*y+(sizemult[1]/2)-(text.get_height()/2)))
    pygame.display.flip()
