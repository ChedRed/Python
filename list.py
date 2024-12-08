data = input("Input a list separated by commas")

data = data.split(",")

temp = []
for i in range(len(data)):
    if data[i] not in temp: temp.append(data[i])
print(temp)
print(len(temp))