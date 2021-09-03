from random import randrange


class Player:
    # Set defaults for new player classes
    def __init__(self):
        self.level = 1
        self.current_xp = 0
        self.hp = 20
        self.min_range = 3
        self.max_range = 9
        self.strength = randrange(self.min_range, self.max_range)

    # Function to calculate attack based on level
    def roll_attack(self):
        self.strength = randrange(self.min_range + self.level, self.max_range + self.level)
        return self.strength

    def get_stats(self):
        return {"level": self.level, "hp": self.hp, "strength": self.strength}

    def add_exp(self, exp):
        self.current_xp += exp
        # Check if level up is needed
        leveled_up = False
        if self.current_xp >= 10 and self.current_xp < 20:
            self.level = 2
            self.hp = 31
            self.min_range = 4
            self.max_range = 10
            self.strength = randrange(self.min_range, self.max_range)
            leveled_up = True
        elif self.current_xp >= 20 and self.current_xp < 30:
            self.level = 3
            self.hp = 39
            self.min_range = 5
            self.max_range = 11
            self.strength = randrange(self.min_range, self.max_range)
            leveled_up = True

        if leveled_up:
            print(f"\nYou have leveled up to level {self.level}!")


# New player
Adventurer = Player()
# New enemy
Imp = Player()
# Set imp max range
Imp.max_range = 5


print("You enter a cave to eliminate the demons. You have been ordered by a nearby towns Mayor to complete this task.")
print("As you enter a cave, the first room contains a small, flying creature. You ready your iron blade.")
input("\nEnter any key to commence battle: ")
print("\nThe small creature see you and rushes to attack!")

while Imp.hp >= 1 or Adventurer.hp >= 1:
    # Execute function in player to get random value
    input("\nEnter a key to roll an attack: ")
    Imp.hp -= Adventurer.roll_attack()
    print("You inflict:", Adventurer.strength, "damage. The Imp has", Imp.hp, "health remaining.")
    # Check if Imp is still alive
    if Imp.hp <= 0:
        break
    Adventurer.hp -= Imp.roll_attack()
    print("You take:", Imp.strength, "damage. You have", Adventurer.hp, "health remaining.")
    if Adventurer.hp <= 0:
        print("\nYou have fallen...")
        exit()

Adventurer.add_exp(5)
print("\nYou have won the battle and gained 5 XP!")
print(f"Current XP: {Adventurer.current_xp}")
