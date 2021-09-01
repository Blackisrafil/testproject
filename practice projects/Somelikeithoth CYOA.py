import random

player_hp = 50
enemy_hp = 10
boss_hp = 15
loot = 0

name = input("Enter a name: ")

print("You have been given a bow and some arrows and have been tasked with one goal: Defeat the boss in the cave.")
print("You enter the cave and find footprints that leads to a path going to the right.")
choice_one = input("Should you continue right? (Y / N) ").lower()

if choice_one == "y":
    print("\nYou've decided to head right towards the footprints. While walking you hear a noise in the distance")
    print("and you come across blood on the walls. An enemy is close. You draw your bow and prepare to strike.")
    print("A shadowy figure emerges from the distance. You ready your bow, set aim and fire. The enemy spots you")
    print("and unsheathes a weapon of his own.")
    player_attack = random.randint(5, 15)
    enemy_attack = random.randint(1, 10)
    player_hp -= enemy_attack
    enemy_hp -= player_attack
    print(f"\n{name}'s HP: {player_hp}")
    print(f"Enemy HP: {enemy_hp}\n")
    if enemy_hp <= 0:
        loot += 100
    else:
        print("You withdraw more arrows and continue shooting projectiles. The enemy is quick, and returns fire.\n")
        player_attack = random.randint(5, 20)
        enemy_attack = random.randint(1, 10)
        player_hp -= enemy_attack
        enemy_hp -= player_attack
        print(f"\n{name}'s HP: {player_hp}")
        print(f"Enemy HP: {enemy_hp}\n")
        loot += 100
    print(f"*{name} picked up {loot} gil*\n")
    print("You've defeated the enemy that was protecting the boss. Nice job! Now it's time to move forward.\n")
    print("It also looks like you have enough gil to afford a potion.")
    heal = input("Would you like to restore some health before moving forward? (Y / N) ")

    if heal == "y" and loot == 100:
        restore_health = random.randint(1, 5)
        player_hp += restore_health
        loot -= 100
        print(f"\n*{name} gained {restore_health} HP*")
        print(f"{name}'s HP: {player_hp}")
        print(f"Current Gil: {loot}\n")
    else:
        print("Let's not waste any more time.\n")
    print("There are a few paths that lead toward the back of the dungeon, where the bosses lair resides.")
    print("Let's gather our scattered arrows and see if we can figure out which way is forward.\n")
    print("You wander the cave a bit more and find a few bits of linen. Could it be from a fallen comrade?\n")
    print("After taking a few more steps forward you begin to hear some music in the background.")
    print("The enemy is close. You get your bow out and prepare for the kill shot.")
    print("You take aim. If you're lucky you'll get a nice head shot and it will all be over.")
    choice_two = input("Are you ready? (Y / N) ").lower()

    if choice_two == "y":
        player_attack = random.randint(1, 20)
        boss_attack = random.randint(10, 25)
        player_hp -= boss_attack
        boss_hp -= player_attack
        print(f"{name}'s HP: {player_hp}")
        print(f"Boss HP: {boss_hp}\n")
        if boss_hp <= 0:
            print("Critical hit!")
        else:
            print(f"You just lost {boss_attack} HP! This guy is good, much better than the last enemy you fought.")
            print("Regardless, it's imperative that you survive and take this enemy out.")
            player_attack = random.randint(10, 20)
            boss_attack = random.randint(5, 15)
            player_hp -= boss_attack
            boss_hp -= player_attack
            print("\n*woosh* *woosh*")
            print("\nJust a bit more...")
            print(f"\n*{name} loses {boss_attack} HP*")
            print(f"\n{name}'s HP: {player_hp}")
            print(f"Boss HP: {boss_hp}")
        print("\nLooks like it's all over now. The boss has been defeated and we can go home.")
        print("*final fantasy victory theme plays*")
    else:
        print("\n*sigh* I knew you weren't ready.")
else:
    print("\nI guess you're scared?")