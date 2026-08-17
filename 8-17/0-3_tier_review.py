import random 

# Even/odd + random

# TODO 1: generate 5 random numbers in a loop, and for each one print 
# whether its even or odd

for i in range(5):
    rnum = random.randint(1, 101)
    
    if rnum % 2 == 0:
        print(f"{rnum} is even.")
    else:
        print(f"{rnum} is odd")
        
print()

# Side random practice 


prizes = ["Teddy Bear", "Giant Foam Finger", "Keychain", "Mystery Box"]

def prize_selector():
    selection = random.choice(prizes)
    print(f"You won a {selection}!")

prize_selector()

print()

lucky_number = random.randint(1, 11)

print("Rolling for a lucky number...")
if lucky_number % 2 == 0:
    print(f"Lucky number {lucky_number} is even! You win an extra $5!")
else:
    print(f"Lucky number {lucky_number} is odd! No extra bonus this time.")


print()

# TODO 2: Pring a right triangle of asterisks, 5 rows tall, each row has 
# one *, and so on. 

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print()

# TODO 3: Given a list, write a comprehension that only returns names 
# containing "web"

names = ["web01", "db01", "cache01", "web02"]

new_list = [x for x in names if "web" in x]
print(new_list)

# Return only the negative numbers, doubled.

nums = [3, -1, 4, -5, 9, -2]

new_list = [x * 2 for x in nums if x < 0]
print(new_list) 

print()

# TODO 4: Given any list of numbers, compute the average in one line 
# using sum() and len()

numbers = [5, 28, 194, 25]

average = sum(numbers) / len(numbers)

print(average)

# TODO 5: given two lists, use zip to build a dictionary {name: score} pairing
# them with dict(zip())

names = ["a", "b", "c"]
scores = [90, 85, 77]

new_dict = dict(zip(names, scores))
print(new_dict)

print()

# TODO 6: Given a list, use sorted with key=lambda to sort the strings by 
# length instead of alphabetically. 

words = ["kiwi", "banana", "fig", "apple"]

sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words)

# Do more, this had to be reffed. 

