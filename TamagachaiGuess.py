def setupGame():
    petName = "Jack"
    water = 100
    energy = 100    
    happiness = 100
    action = "4"
    while(action != "0"):
        if(action != "0" ):
            print("What do you want to do?")
            print("(0) Exit Game"),
            print("(1) Play with " +petName)
            print("(2) Give " +petName+ " water")
            print("(3) Feed " +petName)
            print("Water: "+str(water)+". Saturation:"+str(energy)+". Happiness: "+str(happiness)+".")
            action = input()
        if(action == "1"):
            if(water > 0):
                if(energy > 0):
                    water -= 5
                    energy -= 20
                    happiness += 30
                    if(happiness > 99):
                        print("You tossed a ball , "+petName+" chased the ball. It's happiness was maxed out.")
                        if(happiness > 100):
                           happiness = 100
                    else:
                        print("You tossed a ball , "+petName+" chased the ball. It gained 30 happiness.")
        elif(action == "2"):
            if(energy > 0):
                water += 20
                energy -= 1
                if(water > 99):
                    print("You gave your pet water. "+petName+"'s water was maxed out.")
                    if(water > 100):
                        water = 100
                else:
                    print("You gave your pet water. "+petName+" gained 20 water.")
        elif(action == "3"):
            energy += 20
            if(energy > 99):
                print("You fed your pet. "+petName+"'s saturation was maxed out.")
                if(energy > 100):
                    energy = 100
            else:
                print("You fed your pet. "+petName+" gained 20 saturation.")
        else:
            pass
        if(energy < 1):
            print("Your dog fainted to lack of saturation.")
            action = 0
        if(water < 1):
            print("Your pet fainted to lack of water.")
            action = 0
    print("The game was quit.")
setupGame()