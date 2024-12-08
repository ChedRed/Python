import random
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole()

percent_chance = input("Insert a chance with percent sign\n")
time_period = int(input("Insert a duration (Time between each percent chance is calculated)\n"))
time_label = input("Insert a label for time\n")
iterations = int(input("Insert a maximum iteration count\n"))

chanceb = ""
for i in range(len(percent_chance)-1):
    chanceb += percent_chance[i]
chance = float(chanceb)/100

true_times = 0
wait_time = 0

for i in range(iterations):
    if random.random() <= chance: true_times += 1
    wait_time = 100/(true_times/(i+1)*100)

print(str(true_times),"/",i+1,"\n", str(true_times/(i+1)*100),"%")