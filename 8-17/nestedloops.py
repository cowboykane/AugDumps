# what dude

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

print()

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

pattern = input("Insert symbol for pattern: ")

for i in range(1, 10):
    for j in range(i):
        print(pattern, end="")
    print()