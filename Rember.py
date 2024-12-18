import random as rand
import copy
import os

filines = open("Rember", "r").readlines()
answers = [each.strip().split(" ") for each in filines]


def clear():
    print("\033[H\033[J")


# print(answers)
while True:
    questions = copy.deepcopy(answers)
    realround = 0
    for i in range(len(questions)):
        for j in range(len(questions[i])):
            realround += 1
            if realround > 4:
                realround = -1
            if rand.random() * 4 < realround:
                questions[i][j] = "___"
                if answers[i][j][-1] in ",.?!;:":
                    questions[i][j] += answers[i][j][-1]
                realround = -1


    current = 0
    while True:
        clear()
        if current >= len(questions):
            break
        print("Type the word to fill in the blank!\n")
        final = False
        finaltwo = False
        finalprint = ""
        for i in range(len(questions[current])):
            if i == 0:
                finalprint += questions[current][i]
            elif i > len(answers[current]) - 3 or answers[current][i][0] in "0123456789":
                final = True
            else:
                if (i % 4 == 0):
                    finalprint += "\n"+questions[current][i]
                else:
                    finalprint += " "+questions[current][i]
            if final:
                if finaltwo:
                    finalprint += " "+questions[current][i]
                else:
                    finalprint += "\n  "+questions[current][i]
                    finaltwo = True
        print(finalprint)
        response = input("\nWhat comes next?\n > ")
        broke = False
        for i in range(len(questions[current])):
            if questions[current][i][0:3] == "___":
                questions[current][i] = response
                if answers[current][i][-1] in ",.?!;:":
                    questions[current][i] += answers[current][i][-1]
                broke = True
                break


        broke = False
        for i in range(len(questions[current])):
            if questions[current][i] == "___":
                broke = True
                break
        if not broke:
            current += 1


    clear()
    current = 0
    final = False
    finaltwo = False
    finalprint = ""
    for j in range(len(answers)):
        final = False
        finaltwo = False
        finalprint = ""
        for i in range(len(answers[j])):
            if answers[j][i].lower() != questions[j][i].lower():
                finalprint += "\033[31m"
            if i == 0:
                finalprint += answers[j][i]
            elif i > len(answers[j]) - 3 or answers[j][i][0] in "0123456789":
                final = True
            else:
                if (i % 4 == 0):
                    finalprint += "\n"+answers[j][i]
                else:
                    finalprint += " "+answers[j][i]
            if final:
                if finaltwo:
                    finalprint += " "+answers[j][i]
                else:
                    finalprint += "\n    "+answers[j][i]
                    finaltwo = True
            if answers[j][i].lower() != questions[j][i].lower():
                finalprint += "\033[0m"
        print(finalprint+"\n")
    input("Hit return to try again!")
