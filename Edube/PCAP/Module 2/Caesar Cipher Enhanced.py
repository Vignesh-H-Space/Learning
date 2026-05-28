# Step 1: Get the text to encrypt
text = input("Enter text to encrypt: ")

# Step 2: Force the user to enter a valid shift value (1-25)
while True:
    try:
        # Try to convert the input to an integer
        shift = int(input("Enter shift value (1-25): "))
        
        # Check if it falls within the allowed range
        if 1 <= shift <= 25:
            break # Exit the loop, we have a valid number!
        else:
            print("Error: Shift value must be between 1 and 25.")
            
    except ValueError:
        # If int() fails (e.g., they typed "apple" or "2.5"), catch the crash
        print("Error: Invalid input. Please enter a whole number.")

# Step 3: Encrypt the text
cipher = ""

for char in text:
    # Check if the character is a letter
    if char.isalpha():
        # Determine the math base depending on upper or lower case
        if char.isupper():
            base = ord('A')
        else:
            base = ord('a')
            

# Step 4: Print the final result
print(cipher)