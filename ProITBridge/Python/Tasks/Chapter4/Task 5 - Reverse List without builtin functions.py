# Task 5 - Reverse List without builtin functions

# Reverse a list without using the builtin functions

list1 = [int(x) for x in input("Enter numbers with space ").split()]
letter = []
word = 0
while len(list1) > 0 :
    word = list1.pop()
    letter.append(word)
print(letter)


