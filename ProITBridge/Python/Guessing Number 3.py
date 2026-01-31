# Guessing Number 
# While Loop 

Secret_Number = 56
while True :
    n = int(input("Enter a number between 1 to 100 "))
    if(n==Secret_Number):
        print("You have guessed correct ")
        break
    else:
        print("Wrong guess, kindly guess again")
        
