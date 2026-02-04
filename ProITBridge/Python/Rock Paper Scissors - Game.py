# Rock Paper Scissors - Game 

''' Objective:
Build a simple Rock-Paper-Scissors game where the player competes with the computer.
 This task will test your understanding of:
● Input/output
● Conditional logic
● Random module
● Loops
● Exception handling


Instructions:
1.The user should enter their choice: rock, paper, or scissors.
2.The computer should randomly select one of these.
3.Compare both and print who wins.
4.Ask if the player wants to play again- if yes, repeat; if no, exit.
5.Handle invalid inputs gracefully using try-except or condition checks. '''

import random
print ("Welcome to Rock Paper Scissors Game")
print("Select one among the following : rock, paper, scissors")
options = ["rock","paper","scissors"]
to_continue = 'N'
user_selection = input("Enter your choice: ")
while (to_continue.lower) == 'q':
    try : 
        if (user_selection not in options):
            print("Select proper choice ")
        else :
            computer_selection = random.choice(options)
            if(computer_selection == user_selection):
                print("The battle is drawn ")
            elif (user_selection == "rock"):
                if (computer_selection == "paper"):
                    print("User has lost ")
                else :
                    print("User won ")
            elif (user_selection == "paper"):
                if (computer_selection == "scissors"):
                    print("User has lost ")
                else :
                    print("User won ")
            else :
                 if (computer_selection == "scissors"):
                    print("User has lost ")
                 else :
                    print("User won ")
        
    except ValueError:
        print ("Enter proper value (rock,paper,scissors) with proper spelling ")
        
print("Do you want to continue ? ")
to_continue = input("If no, enter Q. If yes, enter anything else ")    