# Guessing Number 
# For Loop (7 Iterations )

Secret_Number = 56
for i in range (0,7):
    n = int(input("Enter a number between 1 to 100 "))
    if(n==Secret_Number):
        print("You have guessed correct ")
        break
    else:
        print("Wrong guess, kindly guess again")
        
