#---------------------------------------------
import os
import random
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole()
#---------------------------------------------
while True:
    input = input('Truth or Dare?')
    if input.lower() == 'truth':
        e=1
    elif input.lower() == 'dare':
        e=2
    else:
        