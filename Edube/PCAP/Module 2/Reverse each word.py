text = input("Enter a sentence: ")

words = text.split()

for word in words:
    print(word[::-1], end=" ")