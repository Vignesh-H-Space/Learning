# Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

# For example:

# if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)
# Hints:

# you should use the two-argument variants of the pos() functions inside your code;
# don't worry about case sensitivity.

# Step 1: Get user inputs
word = input("Enter the word: ").upper()
text = input("Enter the combination of characters: ").upper()

# Step 2: Initialize variables
is_hidden = True
start_index = 0

# Step 3: Loop through each character in the target word
for char in word:
    # Use the two-argument find() to search starting from our current position
    found_index = text.find(char, start_index)
    
    if found_index == -1:
        # The character was not found in the remaining text
        is_hidden = False
        break
    
    # Update the start_index so the next letter search begins 
    # strictly AFTER the letter we just found
    start_index = found_index + 1