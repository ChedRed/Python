import datetime
from pathlib import Path

def clearConsole():
    import os
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def clearConsoleOnce():
    print ("\033[A\033[A")

clearConsole()

while True:
    print("Insert folder to scan:")
    folder = input("").strip()
    # if Path(folder).exists():
    break
    # else:
    #     print("Invalid folder path. Please try again.")

print("\nType the text you want to scan:")
text = input("").strip()
print("")

time = datetime.datetime.now()

def getCompletionTime(startTime):
    time2 = datetime.datetime.now()
    timeMessage = time2 - startTime
    return timeMessage

matchcountes = 0
matchingText = []
folderPath = Path(folder)

print("Scanning folder:", folderPath, "\n\n")

def search_text_in_files(folder_path):
    for file_path in folder_path.glob('**/*'):
        if file_path.is_file() and not file_path.suffix == '.app':
            clearConsoleOnce()
            print("Searching '" + str(file_path) + "'")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    for line in lines:
                        if text in line:
                            matchingText.append(str(file_path))
                            matchcountes += 1
                            print("Found in '" + str(file_path) + "'")
                            break
            except:
                pass
        elif file_path.is_dir() or file_path.suffix == '.app':
            search_text_in_files(file_path)

search_text_in_files(folderPath)

endTime = getCompletionTime(time)

print("\nCompleted scan. Results:")
for match in matchingText:
    print(match)

print("Operation time:", endTime)
