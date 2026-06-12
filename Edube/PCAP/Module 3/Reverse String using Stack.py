stack = []

text = input("Enter a string: ")

for ch in text:
    stack.append(ch)

reversed_string = ""

while stack:
    reversed_string += stack.pop()

print("Reversed String:", reversed_string)