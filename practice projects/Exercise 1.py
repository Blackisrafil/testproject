from random import randrange

# Here it starts

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


character_stats = False

imp_hp = 20

print("You enter a cave to eliminate the demons. You have been ordered by a nearby towns Mayor to complete this task.")
print("As you enter a cave, the first room contains a small, flying creature. You ready your iron blade.")
input("\nEnter any key to commence battle: ")
print("\nThe small creature see you and rushes to attack!")

while imp_hp >= 1:
    imp_strength = randrange(3, 5)
    if current_xp == 0:
        Adventurer = Player(1, 0, 20, randrange(3, 9))
    if current_xp >= 10:
        Adventurer = Player(2, 10, 31, randrange(4, 10))
    if current_xp >= 20:
        Adventurer = Player(3, 20, 39, randrange(5, 11))
    input("Enter a key to roll an attack: ")
    battle = imp_hp - Adventurer.strength
    print(battle)

# Here are the changes.




