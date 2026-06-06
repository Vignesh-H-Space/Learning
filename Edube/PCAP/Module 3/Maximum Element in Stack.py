stack = [12, 45, 7, 89, 23]

max_num = stack[0]

for item in stack:
    if item > max_num:
        max_num = item

print("Maximum:", max_num)