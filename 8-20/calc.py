# Really simple calculator

print("This is a really simple calculator!\n")

while True:
    try: 
        num1 = int(input("Insert num1: "))
        num2 = int(input("Insert num2: "))
    except ValueError:
        print("Error! not an integer.")
        continue
    
    operation = input("Input an operation: ")
    
    match operation:
        case "+" | "addition" | "add":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}\n")
        case "-" | "Substraction" | "minus":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}\n")
        case "*" | "multiplication" | "multiply":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}\n")
            
        case "/" | "division" | "divided by":
            try:
                result = num1 / num2
                print(f"{num1} ÷ {num2} = {result}\n")
            except ZeroDivisionError:
                print("Error! Cannot devide by zero!")
                
        case _:
            print("Not an operation.")
        
    while True:
        user_prompt = input("Play again? (y/n): \n")
        
        if user_prompt == "y":
            break
        elif user_prompt == "n":
            print("Thank you for using really simple calculator!")
            exit()
        else:
            print("Thats not a valid input!")
