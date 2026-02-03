# Rock Paper Scissors - Game 

''' Objective:
Build a simple Rock-Paper-Scissors game where the player competes with the computer.
 This task will test your understanding of:
●Input/output
●Conditional logic
●Random module
●Loops
●Exception handling|


Instructions:
1.The user should enter their choice: rock, paper, or scissors.
2.The computer should randomly select one of these.
3.Compare both and print who wins.
4.Ask if the player wants to play again- if yes, repeat; if no, exit.
5.Handle invalid inputs gracefully using try-except or condition checks. '''

import random
print ("Welcome to Rock Paper Scissors Game")
list = ["rock","paper","scissors"]
while True : 
    user_selection = input("Enter your choice: ")
    try : 
        if (user_selection not in list):
            print("Select proper choice")
        else :
            if (user_selection == "rock"):
            
        
    except ValueError:
        print ("Enter proper value")