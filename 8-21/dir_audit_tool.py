import os

# Scan a folder tree recursively with os.walk, report:
# file counts, sizes (os.getsize), write the findings into a log file.

# Create a target folder to scan, create a log file path
# to write results to, print running total

folder = "8-21/logs"
files = os.listdir(folder)


import os

for root, dirs, files in os.walk("8-21/logs"):
    for file in files:
        full_path = os.path.join(root, file)
        check_size = os.path.getsize(full_path)
        print(f"{file}: {check_size} bytes")