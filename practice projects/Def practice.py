Boss = False
You = 5
Enemy = 5
Boss_hp = 10

while Enemy == 5:
  print("Enemy still stands")
  Attack = int(input("Please choose a number: "))

  if Attack >= 5:
    print("You defeated it!")
    Enemy = 0
    break

  elif Attack <= 5:
    print("You did not do enough damage.")

if Enemy == 0:
  Boss = True

while Boss == True:
  print("The boss stands before you")
  Attack = int(input("Please choose a number: "))

  if Attack >= 10:
    print("The boss falls")
    print("Congratulations!")
    break

  elif Attack <= 10:
    print("the boss survives and counters! Deals 3 damage!")
    You = You - 3

  if You <= 0:
    print("YOU DIED")
    exit()




