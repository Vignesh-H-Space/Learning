# Guessing Number Part 6

# Generate Random Secret Number
# Number should be 1-100, if it is not, then pop error 
# Should give options like Number is lesser or greater than guessed number 
# Give total number of attempts to the user
# Say that the total number of attempts exceeded 

import random 
Secret_Number = random.randint(1,100)
while(True):
    n = int(input("Enter a number between 1 to 100 \n"))
    if(n>100 or n <1):
        print("The number you have entered is not falling under 1 to 100. Kindly enter the number between the interval 1 to 100")
    elif(n>Secret_Number):
        print("The number you have entered is greater than the secret number")
    elif(n<Secret_Number):
        print("The number you have entered is lesser than the secret number")
    else:
        print(f"Your guess is correct")
        break

