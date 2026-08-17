log_line = "2026-08-14 ERROR Disk failure on web01"

line = log_line.split()

date = line[0]
level = line[1]

for log in log_line:
    print(date)
    print(level)