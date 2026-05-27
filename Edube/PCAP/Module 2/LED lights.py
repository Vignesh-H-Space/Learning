def display_led_number(number_str):
    # Step 1: Define the patterns for each digit (0-9)
    # Each digit is represented as a list of 5 strings (one for each row)
    digits = [
        ["###", "# #", "# #", "# #", "###"], # 0
        ["  #", "  #", "  #", "  #", "  #"], # 1
        ["###", "  #", "###", "#  ", "###"], # 2
        ["###", "  #", "###", "  #", "###"], # 3
        ["# #", "# #", "###", "  #", "  #"], # 4
        ["###", "#  ", "###", "  #", "###"], # 5
        ["###", "#  ", "###", "# #", "###"], # 6
        ["###", "  #", "  #", "  #", "  #"], # 7
        ["###", "# #", "###", "# #", "###"], # 8
        ["###", "# #", "###", "  #", "###"]  # 9
    ]
    
    # Step 2: Loop through each of the 5 rows
    for row_index in range(5):
        line = "" # Create an empty string to build the current row
        
        # Step 3: Loop through each digit character in the user's input string
        for char in number_str:
            # Convert the character (e.g., '1') to an integer index (e.g., 1)
            digit_index = int(char)
            
            # Fetch the specific row part for this digit and add it to our line
            # We add a space " " at the end to separate the digits
            line += digits[digit_index][row_index] + " "
            
        # Print the fully built row before moving to the next row
        print(line)

# Test cases
user_input = input("Enter a non-negative integer: ")
display_led_number(user_input)