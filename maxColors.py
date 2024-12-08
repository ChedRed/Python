from PIL import Image
import os

extensions = [".png",".webp"]
help = """
Commands:

?    compare <similar/all/stop> (int) (int)
     - Compares the first directory of existing
       files with a loaded directory.

?    filter <visible/hidden> <min> <max>
     - Filters out every visible or hidden below
       the min or above the max.

    load (int) (string)
     - Loads a directory.

    search <visible/hidden/name/stop> (int/string)
     - Searches for every visible, hidden, or name
       that matches the serach criteria.

    sort <visible/hidden/name/reverse>
     - Sorts the data by visible, hidden, or name.
     - reverses the sorted data.

    paths
     - Prints all paths and their index

?    unload (int)
     - Unloads a directory.

"""
# >>>>> Clear console
clearConsole = lambda: print("\033c", end="", flush=True)

# >>>>> Check if list or tuple goes this far
def parameterExists(l,n):
    try:
        l[n]
        return True
    except:
        return False

# >>>>> Check if string can convert to int
def tryInt(l):
    try:
        int(l)
        return True
    except:
        return False

# >>>>> Add empty strings to a list in order to fulfill the list assignment index
def expandList(list,newlength):

    return list.extend([""] * newlength)

# >>>>> Return number of files under search query
def searchedFiles(list,query="",item=3):
    itemCount = 0
    if query == "":
        return len(list)
    for i in range(len(list)):
        if item == 1:
            if query == str(list[i][1][0]):
                tempVisible = "".join([" "]*(greatestvis-len(str(list[i][1][0]))))+str(list[i][1][0])
                tempHidden = "".join([" "]*(greatesthid-len(str(list[i][1][1]))))+str(list[i][1][1])
                itemCount += 1
        elif item == 2:
            if query == str(list[i][1][1]):
                tempVisible = "".join([" "]*(greatestvis-len(str(list[i][1][0]))))+str(list[i][1][0])
                tempHidden = "".join([" "]*(greatesthid-len(str(list[i][1][1]))))+str(list[i][1][1])
                itemCount += 1
        elif item == 3:
            if query in str(list[i][0]):
                tempVisible = "".join([" "]*(greatestvis-len(str(list[i][1][0]))))+str(list[i][1][0])
                tempHidden = "".join([" "]*(greatesthid-len(str(list[i][1][1]))))+str(list[i][1][1])
                itemCount += 1
    return itemCount

# >>>>> Print files with their visible and hidden pixels
def printFiles(list,query="",item=3,index=0):
    for i in range(len(list)):
        if item == 1:
            if query == str(list[i][1][0]):
                tempVisible = "".join([" "]*(greatestvis-len(str(list[i][1][0]))))+str(list[i][1][0])
                tempHidden = "".join([" "]*(greatesthid-len(str(list[i][1][1]))))+str(list[i][1][1])
                print(tempVisible+" visible, "+tempHidden+" hidden > "+list[i][0][len(paths[index])+1:len(list[i][0])])
        elif item == 2:
            if query == str(list[i][1][1]):
                tempVisible = "".join([" "]*(greatestvis-len(str(list[i][1][0]))))+str(list[i][1][0])
                tempHidden = "".join([" "]*(greatesthid-len(str(list[i][1][1]))))+str(list[i][1][1])
                print(tempVisible+" visible, "+tempHidden+" hidden > "+list[i][0][len(paths[index])+1:len(list[i][0])])
        elif item == 3:
            if query in str(list[i][0]):
                tempVisible = "".join([" "]*(greatestvis-len(str(list[i][1][0]))))+str(list[i][1][0])
                tempHidden = "".join([" "]*(greatesthid-len(str(list[i][1][1]))))+str(list[i][1][1])
                print(tempVisible+" visible, "+tempHidden+" hidden > "+list[i][0][len(paths[index])+1:len(list[i][0])])

# >>>>> Get all image paths without pixel data
def listFiles(a):
    s = []
    for e in os.listdir(a):
        f = os.path.join(a, e)
        if os.path.isdir(f):
            s.extend(listFiles(f))
        elif os.path.splitext(f)[1] in extensions:
            s.append([f,0])
    return s

# >>>>> Give pixel data to each path
def processFile(p):
    i = Image.open(p).convert('RGBA')
    c = []
    d = []
    for x in range(i.width):
        for y in range(i.height):
            if i.getpixel((x,y)) not in c:
                if i.getpixel((x,y))[3] != 0:
                    c.append(i.getpixel((x,y)))
            if i.getpixel((x,y)) not in d:
                if i.getpixel((x,y))[3] == 0:
                    d.append(i.getpixel((x,y)))
    return (len(c),len(d))

# >>>>> Get input path
while True:
    path = input("Insert a file or folder to search for images > ").strip(" '\"")
    if os.path.exists(path):
        break
    print("Path/file does not exist.")

# >>>>> If its just a file
if os.path.isfile(path):
    print(str(processFile(path)[0])+" visible, "+str(processFile(path)[1])+" hidden")

# >>>>> If its a directory
else:
    paths = [path]
    del path
    searching = False # Is it searching?
    reversed = True # Sort files in reverse?
    sort = 2 # 1: sort by name. 2: sort by visible. 3: sort by hidden.
    greatestvis = 0 # How many spaces the highest 'visible' number has.
    greatesthid = 0 # How many spaces the highest 'hidden' number has.
    searchItem = 0 # 1: search by visible. 2: search by hidden. 3: search by name.
    searchQuery = ""

    # >>>>> Set greatest variables
    allPaths = [listFiles(paths[0])]
    clearConsole()
    print("Found "+str(len(allPaths[0]))+" images within `"+paths[0]+"`")
    for i in range(len(allPaths[0])):
        allPaths[0][i][1] = processFile(allPaths[0][i][0])
        if len(str(allPaths[0][i][1][0])) > greatestvis: greatestvis = len(str(allPaths[0][i][1][0]))
        if len(str(allPaths[0][i][1][1])) > greatesthid: greatesthid = len(str(allPaths[0][i][1][1]))

    # >>>>> set allPaths with default sorting
    allPaths[0] = sorted(allPaths[0], key=lambda x: (x[1],x[0]), reverse=reversed)

    # >>>>> Print file directories with data
    printFiles(allPaths[0])
    while True:
        width = os.get_terminal_size().columns
        reprint = True
        option = input(" > ").lower().split()
        if option:

            # >>>>> Print help menu
            if option[0] == "help":
                print(help)
                reprint = False

            # >>>>> Unload this path
            # elif option[0] == "unload":

            # >>>>> Re-sort allPaths
            elif option[0] == "sort":
                if parameterExists(option,1):
                    for i in range(len(allPaths)):
                        if option[1] == "name":
                            allPaths[i] = sorted(allPaths[i], key=lambda x: x[0], reverse=reversed)
                            sort = 1
                        elif option[1] == "visible":
                            allPaths[i] = sorted(allPaths[i], key=lambda x: (x[1],x[0]), reverse=reversed)
                            sort = 2
                        elif option[1] == "hidden":
                            allPaths[i] = sorted(allPaths[i], key=lambda x: (x[1][1],x[1][0],x[0]), reverse=reversed)
                            sort = 3
                        elif option[1] == "reverse":
                            reversed = not reversed
                            if sort == 1:
                                allPaths[i] = sorted(allPaths[i], key=lambda x: x[0], reverse=reversed)
                            elif sort == 2:
                                allPaths[i] = sorted(allPaths[i], key=lambda x: (x[1],x[0]), reverse=reversed)
                            elif sort == 3:
                                allPaths[i] = sorted(allPaths[i], key=lambda x: (x[1][1],x[1][0],x[0]), reverse=reversed)
                        else:
                            print("Invalid option `"+option[1]+"`")
                            reprint = False
                else:
                    print("No parameter found for `"+option[0]+"`")
                    reprint = False

            # >>>>> Print allPaths with search query
            elif option[0] == "search":
                if parameterExists(option,1):
                    if option[1] == "stop":
                        searching = False
                    else:
                        searching = True
                        if parameterExists(option,2):
                            if option[1] == "visible":
                                searchItem = 1
                                searchQuery = option[2]
                            elif option[1] == "hidden":
                                searchItem = 2
                                searchQuery = option[2]
                            elif option[1] == "name":
                                searchItem = 3
                                searchQuery = option[2]
                            else:
                                print("Invalid option `"+option[1]+"`")
                                reprint = False
                        else:
                            print("No second parameter found for `"+option[0]+"`")
                            reprint = False
                else:
                    print("No parameters found for `"+option[0]+"`")
                    reprint = False

            elif option[0] == "paths":
                print(paths)
                reprint = False

            # >>>>> Set allPaths at index to files from a path
            elif option[0] == "load":
                if parameterExists(option,1):
                    if tryInt(option[1]):
                        if parameterExists(option,2):
                            tempath = option[2].strip(" '\"")
                            if os.path.exists(tempath):
                                clearConsole()
                                allPaths.extend([""] * (int(option[1])+1))
                                paths.extend([""] * (int(option[1])+1))
                                paths[int(option[1])] = tempath
                                allPaths = [listFiles(paths[int(option[1])])]
                                print("Found "+str(len(allPaths[int(option[1])]))+" images within `"+paths[int(option[1])]+"`")
                                for i in range(len(allPaths[int(option[1])])):
                                    allPaths[int(option[1])][i][1] = processFile(allPaths[int(option[1])][i][0])
                                    if len(str(allPaths[int(option[1])][i][1][0])) > greatestvis: greatestvis = len(str(allPaths[int(option[1])][i][1][0]))
                                    if len(str(allPaths[int(option[1])][i][1][1])) > greatesthid: greatesthid = len(str(allPaths[int(option[1])][i][1][1]))
                                allPaths[int(option[1])] = sorted(allPaths[int(option[1])], key=lambda x: (x[1],x[0]), reverse=reversed)
                            else:
                                print("Path/file does not exist.")
                                reprint = False
                        else:
                            print("No second parameter found for `"+option[0]+"`")
                            reprint = False
                    else:
                        print("First parameter must be an integer, not "+option[0][1])
                        reprint = False
                else:
                    print("No parameters found for `"+option[0]+"`")
                    reprint = False

            # >>>>> Commandn't
            else:
                print("Unknown command `"+option[0]+"`")
                reprint = False

        # >>>>> Print all files again ;-;
        if reprint:
            clearConsole()
            print("Found "+str(searchedFiles(allPaths[0],searchQuery,searchItem))+"/"+str(len(allPaths[0]))+" images within `"+paths[0]+"`")
            if searching:
                printFiles(allPaths[0],searchQuery,searchItem)
                print("Successfully ran `"+" ".join(option)+"`")
            else:
                printFiles(allPaths[0])
                print("Successfully ran `"+" ".join(option)+"`")
