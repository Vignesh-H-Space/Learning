stack = []

text = input("Enter a string: ")

for ch in text:
    stack.append(ch)

reversed_text = ""

while stack:
    reversed_text += stack.pop()

