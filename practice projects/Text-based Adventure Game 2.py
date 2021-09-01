
print("You are a super-powered being, able to change the world for better or worse.\nYour decisions decide outcomes.")

old_man = False
Factory = False
River = False
Embassy_building = False

print("Ever since you have awakened to your powers, you have become an unstoppable force.")
print("Many fear the uncertainty you bring, as you have the power to tip the scales of balance in any direction.")
print("Some people revere you, while others fear you. Governments want you either dead or alive.")
print("But they are all powerless, unable to tame the might you possess.")

input("*Enter any key to continue*")

print("You are on your daily travel. Flying overseas and across borders, ignoring any and all international laws")
print("regarding airspace. They can't do a thing to stop you anyway.")
print("You take a look around the barren desert and see an old man. He seems to need assistance travelling.")
print("You fly down to speak to him. He knows who you are and wants nothing to do with you. Tells you to go away.\n")

helporleave = input("Help or leave?").lower()

if helporleave == "help":
    old_man = True
    print("You disregard his rude attitude towards you and conjure some drinking water.")
    print("You then help him by putting him on your back and fly him through the desert to his village.")
    print("As you drop him off and fly away, you see him with a puzzled look, slightly guilty of how he treated you.\n")
elif helporleave == "leave":
    old_man = False
    print("To hell with this old geezer. Who does he think he is? Speaking to YOU like that? If you wanted to, you")
    print("could instantly erase him and whatever backwater village he came from off the face of the planet!")
    print("You give him an look of anger as you fly away, making sure to blow the sand into his eyes with the")
    print("pressure of your energy.\n")

else:
    print("Incorrect input")
    exit()

print("\nAfter that encounter, you decide to fly towards a nearby city. You spot a large building with many armed")
print("personnel at various spots around the area. You decide to check it out. Upon closer inspection you realize")
print("this is a weapons factory. Instruments of war? Something that could never harm you but could destroy the lives")
print("of many. Should you intervene? Screw the laws of this planet. People have suffered enough. Maybe you should")
print("start targeting these places and REALLY make a difference.\n")

factorychoice = input("Destroy or leave?").lower()

if factorychoice == "leave":
    Factory = True
    print("This has nothing to do with you. Various thoughts run through your mind as your float above the building.")
    print("All these laws are in place for a reason. Who knows what will happen if you destroy this building?")
    print("Maybe government tensions will rise, stocks will fall, misinformation on the news, anything.")
    print("As you're pondering, some personnel spot you and aim their guns in your direction, waiting for your move.")
    print("You scoff at them and fly away, leaving them to their devices.\n")
elif factorychoice == "destroy":
    Factory = False
    print("Lets end these fools. These companies have never had to bow to anyone, they have never feared any")
    print("repercussions. You hold up a hand and let loose a huge ball of fire. The fireball travels with great speed")
    print("and hits the building head on, blowing up a huge chunk of their main facilities, leaving nothing but rubble")
    print("and fire. The personnel fire back with guns and missiles. You conjure a shield and easily deflect them.")
    print("You lets them hit you a few times with bullets, just to show you are impervious from their useless weapons.")
    print("Throwing a bolt of lightning at the remaining personnel and soldiers, you finish the job.\n")

else:
    print("Incorrect Input")
    exit()

print("After the factory, you move onto another part of the continent and come across a dried river. You see various")
print("villages nearby who could do well with having a river run through its land. Seeing the nearby sea, you could")
print("either terraform part of the ground and soil to connect a river to it. Or you could conjure up water itself")
print("and create an origin point for it. Either way it could help those poor villagers.\n")

riverchoice = input("Create or leave?").lower()

if riverchoice == "create":
    River = True
    print("You should maybe throw these villages a bone. You wave your hand, and create an infinite source of water in")
    print("one of the dried valleys. You also start to terraform part of the land to connects the sea and rivers.")
    print("The rivers start to fill up and you feel as if you're job is done. You fly away.\n")
elif riverchoice == "leave":
    River = False
    print("This place doesn't need my help. They can survive on their own. I'd rather keep my magic pool topped up")
    print("today. Who knows when I will need it? You fly away as you leave the rivers and area alone.\n")

else:
    print("Incorrect Input")
    exit()

print("Your final stop. You travel to a huge inner city, you seem to remember on the news an embassy. This building")
print("houses a certain political figure who had influence in the government. He was one of the reasons why you were")
print("targeted last month. He even caused idiots to come in and trash your house. Maybe its time for some payback.")
print("But attacking a building like that...it may have huge consequences.\n")

embassychoice = input("Destroy or leave?").lower()

if embassychoice == "destroy":
    Embassy_building = False
    print("You fly towards the building. Some of the occupants outside spot you with confusion in their faces.")
    print("Opening your palm, you concentrate a ball of fire, and hurl it at the building.")
    print("The explosion is much bigger than you intended it to be. You must have put too much power into it.")
    print("Not only has the building been wiped off the map, the surrounding area has been affected.")
    print("Various shops, residential buildings and innocent people were caught in the blast.")
    print("You take one last look at the death and destruction you caused, and fly away.\n")
elif embassychoice == "leave":
    Embassy_building = True
    print("You don't need the headache. Also you have no idea whether there are innocents inside or not. Who are you")
    print("to judge whether someone should die or not? That kind of mentality is dangerous. Best to leave.\n")

else:
    print("Incorrect input")
    exit()

print("You finally get home, back into your dwelling to rest. You reflect on today's events and turn on the news.\n")

if old_man == True:
    print("You remember the old man. You wonder how he's doing? You close your eyes and see him reunite with his")
    print("family. He brings well needed supplies to heal the sick, saving their lives.\n")
else:
    print("The old man flashes in your mind. Somehow you can sense his life-force disappear. His body laying lifeless")
    print("in the barren desert. Never making it back to his village....\n")
if Factory == True:
    print("You see the stock prices of weaponry on a steady rise. Nothing has changed, war still wages with the elite")
    print("profiting with all their blood money invested into these destructive weapons of war.\n")
else:
    print("Oh look, the factory you blew up is on the news. You managed to sever supply lines. The stocks are down.")
    print("Some of these politicians look visibly enraged, spinning the story onto you. And the public is eating it")
    print("up. The stocks have had a major drop.\n")
if River == True:
    print("You see in the international news section. A miracle has happened in another part of the world. Looks like")
    print("A few rivers have appeared directly where dozens of villages needed them, re-invigorating the area.")
    print("A lot of people have been saved.\n")
else:
    print("Other parts of the news flash by, more starving villagers and droughts with the surrounding villages.")
    print("More pleads for charity to the public as the poor need aid. The same thing everyday.\n")
if Embassy_building == True:
    print("You see another conference from the embassy building you passed by. Your favourite politician is spouting")
    print("his rhetoric on you. People seem to be agreeing and his ratings are rising. More public opinion is being")
    print("spun against you. So be it.\n")
else:
    print("The major story has suddenly popped up, eclipsing all the other news. A huge attack has happened within the")
    print("city incurring losses. Currently, over 200 civilians have been killed and counting, with the embassy")
    print("being totally destroyed. This couldn't have been you could it? You didn't realize how many people were")
    print("actually there. Many witnesses claim to have seen an individual flying away. The government has entered")
    print("a state of emergency. A picture of you is now on the screen.\n")