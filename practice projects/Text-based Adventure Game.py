
print("You are in a room with two doors, left and right.\nWhich door will you take?")
leftdoor_rightdoor = input("left door or right door?")

while leftdoor_rightdoor == "left door" or leftdoor_rightdoor == "left":
    print("You enter a brightly-lit hall filled with numerous statues and a long-table in the middle.")
    print("On the table are numerous cutlery and plates set out neatly.")
    print("You see a massive staircase leading upwards towards two huge doors made of fine wood.")
    print("On the left, you see a metal door that is slightly rusted.")
    print("Which path will you take, the metal door or the fine wood door?")
    metaldoor_finewooddoor = input("metal door or fine wood door?")

    while metaldoor_finewooddoor == "metal door" or metaldoor_finewooddoor == "metal":
        print("You open the metal door and hear a rusted creek from the old hinges.")
        print("You look enter and see a dark-lit room furnished with many different sizes of mirrors.")
        print("You see a door leading outside, ending the quest. However one of the mirrors starts to glow")
        print("ominously. A portal opens within the mirror.\nWill you leave the building or enter the mirror?")
        leaveorenter = input("Leave or Enter?")

        while leaveorenter == "enter":
            print("Your body enters the portal and you feel yourself being torn apart, as your soul leaves")
            print("your body.")
            exit()

        while leaveorenter == "leave":
            print("You safely leave the mysterious building. As you step out you find yourself on a familiar road.")
            print("Cars drive by as you take a look around. You recognize this street, as this is your neighbourhood.")
            print("You turn back around to the door and realize that the building is now desolate.")
            print("There is no signs of life and inside, there is only broken furniture.")
            exit()

        else:
            print("Invalid input")
            exit()

    while metaldoor_finewooddoor == "fine wood door" or metaldoor_finewooddoor == "fine" or metaldoor_finewooddoor == "wood door":
        print("You go through the doors and arrive at a peculiar looking chamber fit for a king.")
        print("You see a man dressed in a strange garb.\nHe waves his hand once, and your eyes turn heavy.")
        print("You fall to the ground and close your eyes.")
        exit()

    else:
        print("Invalid input")
        exit()

while leftdoor_rightdoor == "right door" or leftdoor_rightdoor == "right":
    print("You enter the door on the right and step outside into a courtyard. The night sky encompassing the area.")
    print("In the courtyard is a small fountain of an angel, with small bushes surrounding it on either side")
    print("You see a gate leading outside, possibly your way out of this area.\nHowever looking right, you see")
    print("A stone staircase leading into a deep, dark crypt.")
    gate_crypt = input("Enter the gate or crypt?")

    while gate_crypt == "crypt":
        print("Inside the crypt, you see one large tunnel. You follow the tunnel to an open area. There is a man in")
        print("a strange garb in the middle. He looks at you and gestures his hand towards you. Your eyes feel heavy")
        print("and you fall to the ground. Your eyes close as sleep overtakes you.")
        exit()

    while gate_crypt == "gate":
        print("You run towards the gate and force it open. As you open it, you find yourself in a forest. You look")
        print("around and notice the gate behind you has disappeared along with the building you were in. All of a")
        print("sudden it becomes apparent that you are not in your own world anymore. You see various unidentifiable")
        print("creatures. Up in the sky, several large planets are clearly visible....where are you?")
        exit()

    else:
        print("Invalid Input")
        exit()

else:
    print("Invalid input")
    exit()
