# Guessing Number Part 4

# Number should be 1-100, if it is not, then pop error 
# Should give options like Number is lesser or greater than guessed number 
# Give total number of attempts to the user
# Say that the total number of attempts exceeded 

Secret_Number = 56
for i in range (1,11):
    n = int(input("Enter a number between 1 to 100 "))
    if(n>100 or n <1):
        print("The number you have entered is not falling under 1 to 100. Kindly enter the number between the interval 1 to 100")
    elif(n>Secret_Number):
        print("The number you have entered is greater than the secret number")
    elif(n<Secret_Number):
        print("The number you have entered is lesser than the secret number")
    else:
        print(f"Your guess is correct")
        break
if (Secret_Number == n):
    print(f"You have guessed the number {Secret_Number} in {i+1} attempts")
else :
    print("You have exceeded all your attempts")    
        
