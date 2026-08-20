# Server heatlh check simulator
# list of servers, loop trhough each, check if its up or down,
# print status report

import random

server_status = ["UP", "DOWN"]
servers = ["web-01", "web-02", "db-01", "cache-01"]

count_up = 0
count_down = 0


for server in servers:  
    picker = random.choice(server_status)   
    print(f"{server}: {picker}")
    
    if picker == "UP":
        count_up += 1
    else:
        count_down += 1
        
print()
print("-- Summary --")
print(f"Total UP: {count_up}")
print(f"Total DOWN: {count_down}")