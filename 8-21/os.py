import os

# more os module stuff

check_dir = os.listdir("8-21")

for check in check_dir:
    full_path = os.path.join("8-21", check) # builds complete path
    check_size = os.path.getsize(full_path) 
    print(f"{check}: {check_size} bytes")
    
    

# renaming shit 

os.makedirs("Exampledir", exist_ok=True)

os.rename("Exampledir", "SomethingElse")

check_path = os.path.exists("Exampledir")

if check_path:
    print("Path Exists.")
else:
    print("Path doesn't exist.")

with open("random.txt", "w") as f:
    f.write("Better be quieeeeeet now")

os.remove("random.txt")

check_file = os.path.exists("random.txt")

if check_file:
    print("File Exists.")
else:
    print("File doesn't exist.")
    

 
 # os.walk

os.makedirs("Hello", exist_ok=True)
os.makedirs("Hello/Goodbye", exist_ok=True)

with open("Hello/greeting.txt", "w") as f:
    f.write("Something")

with open("Hello/Goodbye/leaving.txt", "w") as f:
    f.write("Something different")
    


for root, dirs, files in os.walk("Hello"):
    print(root, dirs, files)

# root = "Hello", dirs = ['Goodbye'], files = ['greeting.txt']