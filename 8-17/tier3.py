# Tier 3: Lists, tuples, sets 

# TODO 14: given a dictionary, print the unique server names out with set()

servers = ["web01", "web02", "db01", "web01", "cache01"]

print(set(servers))

print()

# TODO 15: given a list of ports, write a comprehension that only returns ports 
# below 1024

ports = [22, 80, 443, 8080, 3306]

newlist = [x for x in ports if x < 1024]

print(newlist)

print()

# TODO 16: Write a function that takes a list of numbers and returns a tuple
# of (min, max, average)

"""
print("Build a list here! q to stop appending.")
comp_list = []

while True:
    user_input = input("Insert numbers to append to a list: ")
    
    if user_input == "q":
        break
    
    comp_list.append(int(user_input))


print(comp_list)

"""

def calc(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    avg = sum(numbers) / len(numbers)
    
    return (minimum, maximum, avg)

calc()

print()

# TODO  17: Given two lists servers and statuses, use zip() to
# print "{server}: {Status}" for each pair 

servers = ["web01", "db04", "cache03"]
statuses = ["ONLINE", "OFFLINE", "ONLINE"]

for server, status in zip(servers, statuses):
    print(f"{server}: {status}")

#TODO 18: Sort a list of dictionaries by using sorted() and lambda()

# skipppppped revisit lambda