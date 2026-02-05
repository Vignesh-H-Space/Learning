# Word Guessing Game (Mini Hangman)
''' 
Objective:
Create a word-guessing game where the player tries to guess the letters of a hidden word.

This will test your:
●Loops
●Conditional logic
●String manipulation
●Exception handling
●Logical thinking

Instructions:
1.Create a list of random words (like “python”, “machine”, “learning”, “bridge”).
2.Randomly select one word for the game.
3.Show the word as blanks (_ _ _ _) and let the player guess one letter at a time.
4.Keep track of wrong guesses (max 6 attempts).
5.End the game when the player either guesses the full word or uses all chances. '''

import random 

word_list = ["python","machine","learning","bridge","number","function","investment"]
word = random.choice(word_list)
length = len(word)
print("Welcome to Word Guessing Game ")
print("You have 6 attemtps to guess the entire word ")
print (f"Hint : The length of the word is {length}")
computer_word = ["_"] * length
print ("".join(computer_word))
for i in range (0,6):
    try : 
        letter = input(f"Enter your {i+1} guess: ").lower()
        if len(letter) > 1 : 
            raise ValueError()
        else :
            for i in range (0,length):
                if word[i] == letter :
                    computer_word[i] = letter 
        print("".join(computer_word))
    except ValueError:
        print ("Enter only one letter at a time")