import os

class errhandles:
    def __init__(self):
        self.errors = []
        self.failed = False

    def storeError(self, data):
        self.errors.append(data)
        self.failed = True

    def tellErrors(self):
        return redefinition.listToString(self.errors, "\n-- Error: ")

class oscommands:
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

class redefinition:
    def listToString(list, separator):
        temp = ""
        for i in range(len(list)):
            if i == 0:
                temp += list[i]
            else:
                temp += separator + list[i]
        return temp

    def filter(inval, whitelist):
        temp = ""
        inval = str(inval)
        for i in range(len(inval)):
            if inval[i] in whitelist:
                temp += inval[i]
        return temp