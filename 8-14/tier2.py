
# Strings

# TODO 10: Take a sentence from input and print:
# Its length, uppercase version, reversed version, and word count.

user_sentence = input("Input a sentence: ")

uppercase = user_sentence.upper()
reversed = user_sentence[::-1]

words = user_sentence.split()
word_count = len(words)

print(f"Uppercase: {uppercase}")
print(f"Reversed: {reversed}")
print(f"Word Count: {word_count}")

print()

# TODO 11: write a function that returns True if the string only 
# contains alphanumerics and hyphens

def is_valid_hostname(name):
    pass

print()

# TODO 12: Given a log line, use slicing and split to to extract just the 
# date, level, and message.

log_line = "2026-08-14 ERROR Disk failure on web01"

line = log_line.split()

date = line[0]
level = line[1]

for log in log_line:
    print(date)
    print(level)

# flopped this parse revisit

# TODO 13: Write a function that takes a filename string and returns True
# only if it ends with .log or .txt endswith()

user_string = input("Insert a string here: ")

print(user_string.endswith((".txt", ".log")))

# Terrible come back to this 
