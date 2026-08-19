def add(x):
    return x + x

add_lambda = lambda x: x + x

# 

words = ["kiwi", "banana", "fig"]
print(sorted(words))

# What if we wanted to srot by LENGTH instead of alphabetically?

# Function example:

def get_length(word):
    return len(word)

print(sorted(words, key=get_length))

print(sorted(words, key=lambda word: len(word)))