word = input("Enter a word: ")

reverse_word = word[::-1]

print("Original Word:", word)
print("Reversed Word:", reverse_word)

if word == reverse_word:

    print("It is a palindrome")

else:

    print("It is not a palindrome")