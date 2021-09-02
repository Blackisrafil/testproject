from random import randrange


class Player:
    def __init__(self, level, current_xp, hp, strength):
        self.level = level
        self.current_xp = current_xp
        self.hp = hp
        self.strength = strength

    def roll_stats(self):
        self.strength = randrange(3, 9), (4, 10), (5, 11)

    def get_stats(self):
        return {"level": self.level, "hp": self.hp, "strength": self.strength}


current_xp = 0

imp_hp = 20

print("You enter a cave to eliminate the demons. You have been ordered by a nearby towns Mayor to complete this task.")
print("As you enter a cave, the first room contains a small, flying creature. You ready your iron blade.")
input("\nEnter any key to commence battle: ")
print("\nThe small creature see you and rushes to attack!")

while imp_hp >= 1 or Adventurer.hp >= 1:
    imp_strength = randrange(3, 5)
    if current_xp == 0:
        Adventurer = Player(1, current_xp, 20, randrange(3, 9))
    if current_xp >= 10:
        Adventurer = Player(2, current_xp, 31, randrange(4, 10))
    if current_xp >= 20:
        Adventurer = Player(3, current_xp, 39, randrange(5, 11))
    # Not sure if this is the best way to execute the code as the player levels up. Did it like this so the random
    # value can be recognized by the While loop.
    input("Enter a key to roll an attack: ")
    imp_hp -= Adventurer.strength
    print("You inflict:", Adventurer.strength, "damage. The Imp has", imp_hp, "health remaining.")
    Adventurer.hp -= imp_strength
    print("You take:", imp_strength, "damage. You have", Adventurer.hp, "health remaining.")
    if imp_hp <= 1:
        break
    if Adventurer.hp <= 1:
        print("You have fallen...")
        exit()

current_xp += 5
print("You have won the battle and gained 5 XP!")
print("Current XP:", + current_xp)
