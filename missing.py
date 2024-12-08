import os

ext = input("Insert file extensions separated by commas (example: .png, .jpeg) > ").strip(" '\"").split(",")
paths = []

print("Enter an empty string to begin search.")
while True:
    try:
        if paths[len(paths)-1] == "":
            paths = paths[0:len(paths)-1]
            break
    except: pass
    paths.append("")
    while True:
        paths[len(paths)-1] = input("Insert a folder path > ").strip(" '\"")
        if os.path.isdir(paths[len(paths)-1]) or paths[len(paths)-1] == "":
            break
        print("Path does not exist.")

allPaths = []

def findFiles(a,b):
    s = []
    for e in os.listdir(a):
        f = os.path.join(a, e)
        if os.path.isdir(f):
            s.extend(findFiles(f,b))
        elif os.path.splitext(f)[1] in b:
            s.append(f)
    return s

for i in range(len(paths)):
    allPaths.append("")
    allPaths[i] = findFiles(paths[i],ext)
