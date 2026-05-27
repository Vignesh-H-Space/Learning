def mysplit(strng):
    # Create an empty list to store our final words
    result = []
    
    # Create an empty string to build the current word character by character
    current_word = ""
    
    # Loop through every character in the string
    for char in strng:
        # Check if the character is a space (or any whitespace)
        if char.isspace():
            # If we hit a space AND we have been building a word, save it!
            if current_word != "":
                result.append(current_word)
                current_word = "" # Reset the builder for the next word

# Test cases
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))