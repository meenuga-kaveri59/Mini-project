import time

def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()
print(r'''
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
print_slow("Welcome to Treasure Island.")
print_slow("Your mission is to find the treasure.")
print_slow('You\'re at a cross road. Where do you want to go?\nType "left" or "right"')
choice1 =input().lower()
if choice1 == "left":
    print_slow("You\'ve come to a lake.\nThere is an island in the middle of the lake.\nType wait to wait for a boat.\nType swim to swim across.")
    choice2=input().lower()
    if choice2 == "wait":
        print_slow("You arrive at the island Unharmed.\nThere are 3 doors infront of you.\nOne red,one yellow and one blue.\nWhich colour do you choose?")
        choice3 = input().lower()
        if choice3 == "red":
           print_slow("You had entered into a dangerous room.\nTo get out of this find a key that is placed in different boxes numbered from 1 to 3")
           print_slow("Choose a box from 1 to 3")
           choice4=input()
           if choice4 == "1":
               print_slow("Your Key opened a way to pass through a bridge which can balance upto 60kgs.\nBut you weigh 65kg including ur luggage")
               print_slow("Do you want to leave urs luggage...Yes/No")
               choice5 = input().lower()
               if choice5 == "yes":
                   print_slow("You entered into treasure room..Decode the following to win the treasure...")
                   print_slow("What is the one thing that is always with you, but you can never see?")
                   choice11 = input().lower()
                   if choice11 == "shadow":
                       print_slow("Congratulations! You won the treasure")
                   else:
                       print_slow("Incorrect Answer....You lost the treasure")
               if choice5 == "no":
                   print_slow("You fell into the river and eaten by crocodiles. Game Over")
           elif choice4 == "2":
                print_slow("You opened a box that contains a bomb.Game Over")
           elif choice4 == "3":
                print_slow("You opened a box that contains a friendly genie.")
                print_slow("The genie offers you a choice between two paths: one leads to the treasure, and the other to certain doom.")
                print_slow("Do you choose the 'left' path or the 'right' path?")
                choice6 = input().lower()  
                if choice6 == "left":
                    print_slow("You carefully walk down the left path and grab treasure! Congratulations!")
                elif choice6 == "right":
                    print_slow("You walk down the right path and fall into a pit of spikes. Game Over.")
                else:
                    print_slow("You chose a path that doesn't exist. Game Over.")
           else:    
               print_slow("You choosed a box that doesn't exist.Game Over")
        elif choice3 == "blue":
            print_slow("You enter a room with a map on the wall. The map shows two routes: one through a dense forest and another through a dark cave.")
            print_slow("Do you choose the 'forest' or the 'cave'?")
            choice7 = input().lower()
            if choice7 == "forest":
                print_slow("You walk through the forest and encounter a wild animal. You manage to escape but get lost. Game Over.")
            elif choice7 == "cave":
                print_slow("You carefully navigate through the dark cave and find the treasure hidden in a secret chamber. Congratulations!")
            else:
                print_slow("You chose a path that doesn't exist. Game Over.")
        elif choice3 == "yellow":
            print_slow("You enter a room filled with giant bugs. To escape, you must solve the following riddle:")
            print_slow("I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?")
            choice9 = input().lower()
            if choice9 == "fire":
                print_slow("The bugs retreat and reveal a hidden passage leading to an underwater cave.")
                print_slow("You dive into the water and swim through the cave, finding a treasure chest at the bottom.")
                print_slow("To open the chest, solve this final riddle:")
                print_slow("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
                choice10 = input().lower()
                if choice10 == "echo":
                    print_slow("The chest opens and you find the treasure inside. Congratulations, you won!")
                else:
                    print_slow("Incorrect answer. The chest remains locked and you run out of air. Game Over.")
            else:
                print_slow("Incorrect answer. The bugs overwhelm you. Game Over.")
        else:
            print("You Choosed a door that doesn't exist. Game over")
    else:
        print("You attacked by a angry trout. Game Over.")
else:
    print("You fell nto a hole.Game Over")
