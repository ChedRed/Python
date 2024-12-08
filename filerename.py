# This program sets the filename for anything within the file to a set prefix, number, and suffix.
# Note how this program will irreversably change the names of the files.
# Also, any file with a different descriminator or without one will be given the set descriminator.

import os
import pathlib
from time import sleep
filename = "pinterest§.png" #resulting filename; anything before '§' is the prefix, and anything after is the suffix

prefix = ""
suffix = ""

setPrefix = True
for i in range(len(filename)):
    if filename[i] != "§":
        if setPrefix:
            prefix += filename[i]
        else:
            suffix += filename[i]
    else: setPrefix = False

print("Input a filepath into the console.")
parentpath = input("Note that only the first set of files will be renamed.\nDirectories within the parent folder will not be considered.\n")
data = os.path.normpath(str(parentpath + "/"))

if data[0] == "'":
    RAMdata = ""
    for i in range(len(data) - 2):
        RAMdata += data[i + 1]
    data = RAMdata

print(len(os.listdir(data)))

for i, f in enumerate(os.listdir(data)):                            # run through all files within parent
    src = os.path.join(data, f)                                     # joins the filepath and filename
    dst = os.path.join(data, ("§" + str(i + 1)))                    # joins the filepath and the new filename
    os.rename(src, dst)                                             # sets the src to dst

print(len(os.listdir(data)))

for i, f in enumerate(os.listdir(data)):                            # run through all files within parent
    src = os.path.join(data, f)                                     # joins the filepath and filename
    dst = os.path.join(data, (prefix + str(i + 1) + suffix))        # joins the filepath and the new filename
    os.rename(src, dst)                                             # sets the src to dst

print(len(os.listdir(data)))