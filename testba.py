i=0

while True:
    print(i)
    for l in range(10):
        if i == l:
            print("end")
            break
    i += 1
    if i > 100:
        break