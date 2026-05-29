# Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 is the digit we searched for and found.

# Your task is to write a program which:

# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
# outputs the Digit of Life for the date.

# Step 1: Ask the user for their birthday
date_str = input("Enter your birthday (in digits): ")

# Clean the input just in case they added spaces
date_str = date_str.replace(" ", "")

# Step 2: Create a loop that keeps running as long as we have more than 1 digit
while len(date_str) > 1:
    
    current_sum = 0
    
    # Step 3: Loop through every individual character in the string
    for char in date_str:
        # Convert the text character to a math number and add it to our total
        current_sum += int(char)
        
    # Step 4: Convert the math sum BACK to a string so the while loop can check its length
    date_str = str(current_sum)

# Step 5: Print the final single digit
print(date_str)