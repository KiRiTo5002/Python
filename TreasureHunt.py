# Treasure Hunt
print(
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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      '''
)
print(
    "Welcome to the treasure hunt players!\nYour mission is to find the treasure!\n I wish you luck on this road full of challanges and traps."
)
start = input("do you want to start?\nYes/No\n")
if start == "yes" or "Yes":
    print("You are standing on a crossroad. which path would you take?\nLeft or Right")
    path1 = input("which path would you walk on?\n")
    if path1 == "Left" or "left":
        print("you have reached upon a river bank.")
        path2 = int(
            input(
                "What would you do brave warrior?\n1.Swim\n2.Wait for a boat\n(Choose 1 or 2)"
            )
        )
        if path2 == 2:
            print(
                "You have reached the other shore.\nThere are three houses.\nwhich House would you enter?"
            )
            path3 = int(input("1.Red\n2.Blue\n3.Yellow"))
            if path3 == 3:
                print("you have found the treasure insde\nYOU WIN!!!")
            else:
                print("You entered a room full of beasts.\n GAME OVER!!!")
        else:
            print("A Sea Searpent blocks you path\nGAME OVER!!!")
    else:
        print("A flame Breathing Dragon Blocks your path.\nGAME OVER!!!")
else:
    print("Please come again.")