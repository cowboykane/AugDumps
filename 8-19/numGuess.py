# Number guessing game 
import random 

rand_num = random.randrange(0, 26)

count = 0

while True:
    guess = int(input("Guess a number: "))
    count = count + 1
    if guess < rand_num:
        print("Go higher!\n")
        
    elif guess > rand_num:
        print("Go lower!\n")
        
    elif guess == rand_num:
        print(f"Correct! you guessed the number in {count} attempt(s).")
        break

