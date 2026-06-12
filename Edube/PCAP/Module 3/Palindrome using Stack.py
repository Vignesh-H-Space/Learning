stack = []

text = input("Enter a string: ")

for ch in text:
    stack.append(ch)

reversed_text = ""

while stack:
    reversed_text += stack.pop()

if text == reversed_text:
    print("Palindrome")
else:
    print("Not Palindrome")