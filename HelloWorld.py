from turtle import *
def setupTurtle(): #Turtle setup in a function
    t = Turtle()
    t.pensize(10000)
    t.pencolor("Black")
    t.speed(100)
    t.pendown()
    t.forward(1)
    return print("Turtle has been setup.")
def moveTurtle():
    t = Turtle()
    print("Select a program please.")
    SelectedProgram = input()
    print("Enter a speed please.")
    speedVar = int(input())
    t.speed(speedVar)
    print("Enter a size please.")
    turtleSize = int(input())
    t.pensize(turtleSize)
    print("Enter a color please.")
    penColor = input()
    t.pencolor(penColor)
    while(True):
        if(SelectedProgram == "Stop"):
            break
        while(True):
            length = 0
            if(SelectedProgram == "Stop"):
                break
            if(SelectedProgram == "OctoSpiral"):
                while(True):
                    length += 1
                    t.right(22.5)
                    t.forward(length)
            elif(SelectedProgram == "SpikeyBall"):
                while(True):
                    length += 1
                    t.forward(length)
                    t.right(length)
            elif(SelectedProgram == "SquareSpiral"):
                while(True):
                    length += 1
                    t.forward(length*length)
                    t.circle(100-length, 90)
            else:
                print("That is not a known program.")
                done()
        t.clear()
        print("Select a program please.")
        SelectedProgram = input()
setupTurtle() 
moveTurtle()