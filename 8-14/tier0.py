
# Essentials Warmup

import random

# TODO 1: Ask user for their name and age as input.

name = input("Insert your Name: ")
age = int(input("Insert your Age: "))
updated_age = age + 10

print(f"Hi {name}, in 10 years you'll be {updated_age}.")

print()

#TODO 2: Take two numbers from input, cast them to float, produce sum, etc.

def float_converter():
    num1 = float(input("Insert num1: "))
    num2 = float(input("Insert num2: ")) 
    
    sum = num1 + num2
    difference = num1 - num2
    quotient = num1 / num2
    product = num1 * num2
    
    print()
    
    print(f"Sum: {sum}")
    print(f"Difference: {difference}")
    print(f"Quotient: {quotient}")
    print(f"Product: {product}")

float_converter()

print()

#TODO 3: Use type to print the data types of 5 defined variables

a = "What"
b = 5
c = 5.0
d = True
e = [1, 2, 3, 4, 5]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print()

# TODO 4: use random, print a number between 1-100, then check if its even or odd.

rand = random.randrange(1, 101)

if rand % 2 == 0:
    print(f"{rand} is an even number.")
else:
    print(f"{rand} is an odd number.")