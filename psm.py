from pathlib import Path as pl
import os

class storage:
    def __init__(self, relative_path="/"):
        if not os.path.exists(str(pl().absolute())+relative_path+"python_storage.ptc"):
            pl.open(str(pl().absolute())+relative_path+"python_storage.ptc")
        self.path = str(pl().absolute())+relative_path+"python_storage.ptc"

    def write_data(self, data, name, key):
        index = 0
        file = []
        temp = 0
        search = True
        with open(self.path,"r") as f:
            while line := f.readline():
                temp += 1
                file.append(line.rstrip())
                print(line.rstrip())
                if line.rstrip() == "[{}]".format(name):
                    print("Name found")
                    index = temp
                if line.rstrip() == "[next]" and index != 0 and search == True:
                    index = temp
                    print(index)
                    search = False
        file.insert(index-1,"[end]")
        file.insert(index-1,data)
        file.insert(index-1,f"[{key}]")
        with open(self.path,"w+") as f:
            for i in range(len(file)):
                f.write(file[i]+"\n")