s = input("Enter brackets: ")

count = 0

for ch in s:
    if ch == "(":
        count += 1
    elif ch == ")":
        count -= 1

    if count < 0:
        break

if count == 0:
    print("Balanced")
else:
    print("Not Balanced")