import datetime
import shutil
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole()

getfolder = input("Insert folder to get files\n")
setfolder = input("Insert folder to overwrite files\n")


time = datetime.datetime.now()
sTimeHr = time.hour
sTimeMn = time.minute
sTimeSc = time.second
sTimeMs = time.microsecond

foldf=""
for i in range(len(getfolder)-2):
    foldf+=getfolder[i+1]
getfolder=foldf

foldf=""
for i in range(len(setfolder)-2):
    foldf+=setfolder[i+1]
setfolder=foldf

clearConsole()
print("SRC:\n" + getfolder + "\nDST:\n" + setfolder)

def getCompletionTime():
    time2 = datetime.datetime.now()
    nTimeHr = time2.hour - sTimeHr
    nTimeMn = time2.minute - sTimeMn
    nTimeSc = time2.second - sTimeSc
    nTimeMs = time2.microsecond - sTimeMs
    timeMessage=""
    if nTimeMn < 0:
        nTimeHr -= 1
        nTimeMn += 60
    if nTimeSc < 0:
        nTimeMn -= 1
        nTimeSc += 60
    if nTimeMs < 0:
        nTimeSc -= 1
        nTimeMs += 1000000
    if nTimeHr > 0:
        timeMessage += str(nTimeHr) + " Hours, "
    if nTimeMn > 0:
        timeMessage += str(nTimeMn) + " Minutes, "
    timeMessage += str(nTimeSc) + " Seconds, "
    timeMessage += "and " + str(nTimeMs) + " Microseconds."
    return timeMessage

#-=-=-=-Main Code-=-=-=-#

filepaths = []
filenames = []
filenum = 0
for path, subdirs, files in os.walk(getfolder):
    for name in files:
        if ".png" in name:
            filenum += 1
            filenames.append(name)
            filepaths.append(os.path.join(path, name))
print("Files detected: " + str(filenum))

filenum = 0
for path, subdirs, files in os.walk(setfolder):
    for name in files:
        if name in filenames:
            shutil.copyfile(filepaths[filenames.index(name)], os.path.join(path, name))
            print("Copied '" + filepaths[filenames.index(name)] + "' to '" + os.path.join(path, name) + ".")
            filenum += 1

endTime = getCompletionTime()
print("Completed file copy. Results:")
print("Total copied files: " + str(filenum))
print("Operation took " + endTime)