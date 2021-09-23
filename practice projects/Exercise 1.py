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
            leveled_up = True
        elif self.current_xp >= 20 and self.current_xp < 30:
            self.level = 3
            self.hp = 39
            leveled_up = True

        if leveled_up:
            print(f"\nYou have leveled up to level {self.level}!")


# New player
Adventurer = Player()
# New enemy
Imp = Player()
# Set imp max range
Imp.max_range = 5

Hellhound = Player()

Hellhound.min_range = 2
Hellhound.max_range = 6
Hellhound.strength = randrange(Hellhound.min_range, Hellhound.max_range)
Hellhound.hp = 22

Oni = Player()

Oni.min_range = 4
Oni.max_range = 9
Oni.strength = randrange(Oni.min_range, Oni.max_range)
Oni_block = 2
Oni_heal_min = 1
Oni_heal_max = 3
Oni_heal = randrange(Oni_heal_min, Oni_heal_max)
Oni.hp = 30

ladder = False

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

input("\nYou take a rest, patching your wounds up.")
Adventurer.hp += 12
print("\nYour health has recovered by 12!")
print("Current health:", Adventurer.hp)

input("\nEnter any key to continue your hunt.")

print("\nYou press on into the dark caves. As you go deeper, you feel the air change and find it hard to breathe.")
print("You see two paths, one right and left. The right path seems to be narrow. The floor is slightly wet.")
print("The left path seems much less welcoming, with a blue hue of light that seems to be emitting down the pathway.")
print("\nWhich path will you take?")


first_crossroad = input("Right or Left?").lower()

if first_crossroad == "right":
    print("You take the much welcoming route down the wet path. It isn't long until you find another demon.")
    print("The demon with two tails turns to look at you. It seems to be a Hell-Hound. It attacks! You ready yourself!")
    while Hellhound.hp >= 1 or Adventurer.hp >= 1:
        input("\nEnter a key to roll an attack: ")
        Hellhound.hp -= Adventurer.roll_attack()
        print("You inflict:", Adventurer.strength, "damage. The Hell-Hound has", Hellhound.hp, "health remaining.")
        if Hellhound.hp <= 0:
             print("\nYou are victorious! Obtained 10 XP!")
             Adventurer.add_exp(10)
             print(f"Current XP: {Adventurer.current_xp}")

             print("Your current Health is: ", Adventurer.hp)
             break

        Adventurer.hp -= Hellhound.roll_attack()
        print("You take:", Hellhound.strength, "damage. You have", Adventurer.hp, "health remaining.")
        Adventurer.hp-= 2
        print("The demons tails grants an extra attack!")
        print("You take: 2 damage. You have", Adventurer.hp, "health remaining.")
        if Adventurer.hp <= 0:
            print("\nYour legs give way...leaving you defenseless.")
            exit()

if first_crossroad == "left":
    ladder = True
    print("You take the less welcoming path and find a room. As you enter it, the doors close shut and the air turns")
    print("hot! You see a half broken ladder leading up into another part of the cave. You'll need to jump high")
    print("to catch it before you burn to death!")
    while ladder == True or Adventurer.hp >= 1:
        print("\nRoll at least 9 or more to survive!")
        input("Enter any button to roll: ")
        ladder_event = randrange(0, 10)
        print(ladder_event)
        if ladder_event <= 8:
            print("You did not jump high enough.")
            print("You have taken 3 damage...")
            Adventurer.hp -= 3
            print("Remaining HP:", Adventurer.hp)
            if Adventurer.hp <= 1:
                print("You have burnt to death...")
                exit()
        else:
            print("You managed to survive the deathtrap!")
            print("You obtain 20 xp!")
            Adventurer.add_exp(20)
            print(f"Current xp: {Adventurer.current_xp}")
            break



print("You manage to keep dragging your feet through the narrow crevices of the cave being careful of any dangers that")
print("may lurk around you.")
input("Enter any key to continue: ")
print("You feel your quest almost coming to an end. As you talk down the dark path, you see a large opening.")
print("A giant demon sees you. It looks to be an Oni-class demon. This one will be a tough fight!")

input("Your stats so far:")
print("Level:", Adventurer.level)
print("Strength:", Adventurer.min_range,",",Adventurer.max_range)
print("Health:", Adventurer.hp)
print("XP:", Adventurer.current_xp)

input("Get ready for the final battle. Enter any key to step forward and fight!")

while Oni.hp >= 1 or Adventurer.hp >= 1:
    input("\nEnter a key to roll an attack: ")
    Oni.hp -= Adventurer.roll_attack() - Oni_block
    print("You inflict:", Adventurer.strength, "damage. Oni blocks for:", Oni_block,"Health!")
    print("Oni has", Oni.hp, " remaining.")
    if Oni.hp <= 0:
        print("You manage to land the final blow...")
        break
    Adventurer.hp -= Oni.roll_attack()
    print("You take:", Oni.strength, "Damage. You have:", Adventurer.hp, "remaining.")
    if Adventurer.hp <= 0:
        print("You take a fatal blow from the mighty demon. You fall to the ground...")
        exit()
    print("\nThe Onis body emits a green aura, it has healed itself!")
    Oni.hp += Oni_heal
    print("The Onis remaining health:",Oni.hp)

input("The Oni falls as you land your finishing strike.")
print("\nYou stand victorious, and your quest has come to an end. You proudly return to the town.")
print("~Fin~")
