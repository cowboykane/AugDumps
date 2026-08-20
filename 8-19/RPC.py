import random 

player_score = 0
computer_score = 0
round = 0

comp_list = ["rock", "paper", "scissors"]

beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


while player_score < 3 and computer_score < 3:
    round = round + 1
    player_choice = input("Rock, paper, or scissors: ").lower().strip()
    print(f"Player: {player_choice}")
    computer_choice = random.choice(comp_list)
    print(f"Computer: {computer_choice}")
    
    if player_choice == computer_choice:
        print(f"Tie!")
    
    elif beats[player_choice] == computer_choice:
        print("Player Wins!\n")
        player_score = player_score + 1
    
    else:
        print("Computer wins!\n")
        computer_score = computer_score + 1