import random

# Control FLow & Loops:

# TODO 5: Number guessing game. 1-20, loop with while True, higher, lower, correct--break

num = random.randrange(1, 21)

while True:
    guess = int(input("Insert a number between 1-21: "))
    
    if guess > num:
        print("Lower!")
    elif guess < num:
        print("Higher!")
    else:
        print()
        print(f"Correct! The number is {num}.")
        break

print()

# TODO 6: IDK fizzbuzz

# TODO 7: try/except block that keeps asking for an int until it gets one. 

while True:
    try:
        num1 = int(input("Insert a number: "))
        num2 = int(input("Insert another number: "))
        product = num1 * num2
        print(product)
    except ValueError:
        print("Thats not an integer. Try again.")
        continue
    break
    
print()

# TODO 8: Use match to take input like "start", "stop", "status" and print
# a corresponding fake action method. Can I get more detail on that?

cmd = input("Enter command: ")

match cmd:
    case "start" | "Start":
        print("Starting service...")
    case "stop" | "Stop":
        print("Stopping service...")
    case "status" | "Status": 
        print("Retreiving status...")
    case "restart" | "Restart":
        print("Restarting service...")
    case _:
        print("Unrecognized Command. Available commands are:")
        print("""
              Start
              Stop
              Status
              Restart
              """)

print()

# TODO 9: Print a multiplication table from 1-5 using for i in range(1, 6)
# nested inside for j in range(1, 6)


for j in range(1, 6):
    for i in range(1, 6):
        print(j * i, end="\t")
    print()  

