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
            
        # The Math: 
        # 1. Find the letter's position from 0-25 (ord(char) - base)
        # 2. Add the shift
        # 3. Use Modulo 26 (% 26) to wrap around if it goes past 'z'
        # 4. Add the base back to get the real ASCII value
        new_char_code = (ord(char) - base + shift) % 26 + base
        
        # Convert the new ASCII number back to a letter and add to cipher
        cipher += chr(new_char_code)
    else:
        # If it's a space, number, or punctuation, just drop it in unchanged
        cipher += char

# Step 4: Print the final result
print(cipher)