from PIL import Image
import os
while True:
    inf = input("Insert a file path or directory to scan image(s)\n > ").strip()
    print(inf)
    if inf[0] == "\"" and inf[len(inf)-1] == "\"":
        inf = inf[1:len(inf)-1]
        print(inf)
    if os.path.exists(inf):
        break

im = Image.open(inf)
print(str(im.width)+", "+str(im.height))
