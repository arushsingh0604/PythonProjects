'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

path = input("You are presented with 2 paths one tha goes left and the other that goes right.\nType L for left and R for right:")
if path == "L":
    print("You've now reached the river")
    swim = input("Would you like to swim across the river or wait?.\nType S for swim and W for wait:")
    if swim == "S":
        print("You've been devoured by the MIDGARD SERPENT!!!.\nGAME OVER")
    else:
        print("You've been carried by the gods to the 3 doors")
        door = input("Which door do you wanna enter.Type R for red, B for blue and Y for yellow:")
        if door == "R":
            print("You've been burned by fire!!!.\nGAME OVER")
        elif door == "B":
            print("You've been eaten by BEASTS!!!.\nGAME OVER")
        elif door == "Y":
            print("You WINNNNNN!!!")
        else:
            print("Door doesn't exist.\n GAME OVER ")
else:
    print("You've fallen into the hole of hell!!!.\nGAME OVER ")


