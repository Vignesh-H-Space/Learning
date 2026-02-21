# Task 4 - Vowels in a String

# Given a String , count the number of vowels present 

word = input("Enter a word: ")
counta = 0
print("The vowels are :",end=" ")
for i in word: 
    if i in 'aeiouAEIOU':
        counta = counta + 1
        print(i,end= " ")
print(f"The total vowels are {counta}")