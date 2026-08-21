import os
import random

log_folder = "8-21/logs"
log_file = os.path.join(log_folder, "server_status.log")

os.makedirs(log_folder, exist_ok=True)

if os.path.exists(log_file):
    print("Previous log found\n")

server_status = ["UP", "DOWN"]
servers = ["web-01", "web-02", "db-01", "cache-01"]

count_up = 0
count_down = 0

with open(log_file, "a") as file:
    for server in servers:   
        picker = random.choice(server_status)   
        print(f"{server}: {picker}")
        file.write(f"{server}: {picker}\n")
        
        if picker == "UP":
            count_up += 1
        else:
            count_down += 1

print("\n--- Status Summary ---")
print(f"Total UP: {count_up}")
print(f"Total DOWN: {count_down}")