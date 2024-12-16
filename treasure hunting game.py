print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the treasure island, your mission is to find the treasure box")

choice1 = input('Which way are you going? Type "Right" or "Left"\n').lower()

if choice1 == "left":
    print(''' _      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
_     _     _     _     _     _     _     _
)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,
_    _    _    _    _    _    _    _    _
)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,
 _       _      _       _      _      _
( `'-.,_( `'-.,( `'-.,_( `'-._( `'-.,( `'-.,
 _    _     _      _
( '-.( '-.,( '-.,_( `'-.,_''')
    print('Now that you\'ve come to this river, would you "Swim" or "Wait" for a boat?" ')
    choice2 = input('Enter your response with "Swim" or "Wait"\n ').lower()
    if choice2 == "wait":
        print("Enter the boat to cross over!....\n Buuum you have to enter one these doors to get your treasure")
        choice3 = input('Choose your preferred door: "Yellow", "Red", "Blue" \n').lower()
        if choice3 == "yellow":
            print("Congratulations you found the treasure chest")
        elif choice3 == "red":
            print("oops! you just entered a fire room, Game Over!")
        else:
            print("Eiyaah, you just entered a Lion's den, Game Over!")
    else:
        print("You've been eaten by a crocodile, Game Over!")
else:
    print("You choosed the wrong way, Game Over!")
    
