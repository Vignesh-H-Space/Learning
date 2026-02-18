# Task 4 - Vowels in a String

# Given a String , count the number of vowels present 

word = input("Enter a word: ")
word = word.lower()
counta = 0
print("The vowels are :",end=" ")
for i in word: 
    if i == 'a' or i == 'e' or i =='i' or i == 'o' or i== 'u':
        counta = counta + 1
        print(i,end= " ")
print(f"The total vowels are {counta}")