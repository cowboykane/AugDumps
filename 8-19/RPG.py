# Two fighters take turns rolling dice and rolling random damage until 
# one hits 0 HP 

import random 

player1 = input("Insert name for player1: ")
player2 = input("Insert name for player2: ")

HP1 = 50
HP2 = 50

print("Ready...Set...Fight!\n")

round = 0
    
while HP1 > 0 and HP2 > 0:
    round = round + 1
    damage1 = random.randint(1, 15)
    HP2 = HP2 - damage1
    
    print(f"-- Round {round}: Start! --")
    print(f"{player1} hits {player2} for {damage1}!")
    print(f"{player2} HP: {max(0, HP2)}\n")
        
    if HP2 <= 0:
        print(f"{player1} wins the battle!")
        break

    damage2 = random.randint(1, 15)
    HP1 = HP1 - damage2
    print(f"{player2} hits {player1} for {damage2}!")
    print(f"{player1} HP: {max(0, HP1)}\n")
    
    if HP1 <= 0:
        print(f"{player2} wins the battle!")
        break