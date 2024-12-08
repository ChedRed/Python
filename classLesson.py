class PClass:
    def __init__(self, name, strength, speed, maxhealth, maxstamina, defense):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.maxhealth = maxhealth
        self.maxstamina = maxstamina
        self.defense = defense


standard = PClass("Standard",50,50,100,50,30)
rouge = PClass("Rouge",85,60,40,50,20)

class player(PClass):
    def __init__(self,name,pclass):
        self.name = name
        self.pclass = pclass
        self.strength = pclass.strength
        self.speed = pclass.speed
        self.maxealth = pclass.maxhealth
        self.health = pclass.maxhealth
        self.maxstamina = pclass.maxstamina
        self.stamina = pclass.maxstamina
        self.defense = pclass.defense
        self.immune = False

    def damage(self, attacker, strength):
        if not self.immune:
            self.health -= strength / self.defense
            self.health = round(self.health,2)
            return round(strength / self.defense,2)
        return 0

    def attack(self, target):
        self.stamina *= 0.95
        return target.damage(self.name, self.strength * (self.stamina/self.maxstamina))

    def dead(self):
        return self.health <= 0

players = [player("ChedRed",standard),player("Hyper",rouge)]

print(players[0].name + " Vs " + players[1].name)

while True:
    if players[0].speed < players[1].speed:
        print(players[0].name + " attacked for " + str(players[0].attack(players[1])) + " damage.")
        if players[1].dead():
            print (players[0].name + " Wins!")
            break
        print(players[1].name + " is at " + str(players[1].health) + " health.")
        print(players[1].name + " attacked for " + str(players[1].attack(players[0])) + " damage.")
        if players[0].dead():
            print (players[1].name + " Wins!")
            break
        print(players[0].name + " is at " + str(players[0].health) + " health.")
        print("------------------------------------")
    elif players[1].speed < players[0].speed:
        print(players[1].name + " attacked for " + str(players[1].attack(players[0])) + " damage.")
        if players[0].dead():
            if players[0].dead():
                print (players[1].name + " Wins!")
                break
        print(players[0].name + " is at " + str(players[0].health) + " health.")
        print(players[0].name + " attacked for " + str(players[0].attack(players[1])) + " damage.")
        if players[1].dead():
            print (players[0].name + " Wins!")
            break
        print(players[1].name + " is at " + str(players[1].health) + " health.")
        print("------------------------------------")
