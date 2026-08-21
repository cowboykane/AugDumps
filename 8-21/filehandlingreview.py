# File handling review 

import os 

# Opening and creating files

with open("newfile.txt", "w") as f:
    f.write("This is a new file")

with open("8-21/trinket.py", "w") as f:
    print("This is\n", file=f)
    print("an example of\n", file=f)
    print("a line", file=f)

with open("8-21/newfile.txt", "r") as f:
    content = f.read()
    print(content)

with open("8-21/newfile.txt", "r") as f:
    for line in f:
        print(line.strip())
    
with open("8-21/newfile.txt", "a") as f:
    f.write("this is another line in this file\n")

with open("8-21/newfile.txt", "r") as f:
    content = f.read()
    print(content)
    
check_path = os.path.exists("8-21/newfile.txt")

if check_path:
    print("Path exists.")
else:
    print("Path does not exist.")

check_path2 = os.path.exists("8-22/example.py")

if not check_path2:
    print("Path does not exist.")
else:
    print("Path exists.")


os.makedirs("8-22", exist_ok=True) # create folder 

with open("8-22/example.txt", "w") as f: # write to file
    f.write("Hi this is an example\n")
    f.write("This is an ongoing thing it seems\n")

with open("8-22/example.txt", "r") as f: # read file by line
    for line in f:
        print(line.strip())

