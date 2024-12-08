import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole()

class Game:
    Rounds = int(input("Insert number of Rounds.\n"))
    End = False
    Skip = False

class Players:
    P1 = input("Insert player 1 name.\n")
    P2 = input("Insert player 2 name.\n")
    P1_Points = 0
    P2_Points = 0
    ScoreP1 = " "
    ScoreP2 = " "
    Winner = ""

clearConsole()

while Game.End == False:
    if Game.Skip == False:
        print("P1|P2\n")
        for k in range(2 * (Game.Rounds) + 2):
            l=k+1
            if l % 2 == 0:
                print("--|--")
            elif l == 1:
                print(Players.P1[0],"|",Players.P2[0])
            else:
                if Players.P1_Points > (l-2)/2:
                    ScoreP1 = "X"
                else:
                    ScoreP1 = " "
                if Players.P2_Points > (l-2)/2:
                    ScoreP2 = "X"
                else:
                    ScoreP2 = " "
                print(ScoreP1,"|",ScoreP2)
        print(Players.P1_Points,",",Players.P2_Points)
        if (Players.P1_Points < Game.Rounds) & (Players.P2_Points < Game.Rounds):
            Winner = input("Type the name of the player who won a point:\nPlayer 1 (" + Players.P1 + ") or Player 2 (" + Players.P2 + ").\n")
        else:
            Game.End = True
    else:
        Winner = input("'" + Winner + "' is not a player.\nChoose Player 1 (" + Players.P1 + ") or Player 2 (" + Players.P2 + ").\n")
    Game.Skip = (Winner != Players.P1) & (Winner != Players.P2)
    if Game.Skip == False:
        if Winner == Players.P1:
            Players.P1_Points += 1
        else:
            Players.P2_Points += 1
    if Game.End == False:
        clearConsole()
if Players.P1_Points > Players.P2_Points:
    print(Players.P1 + " won!")
else:
    print(Players.P2 + " won!")