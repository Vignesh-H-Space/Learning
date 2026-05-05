# Initializing the variables
a = 1
b = 0

print(f"Before swap: a = {a}, b = {b}")

# The XOR Swap Algorithm
a = a ^ b
b = a ^ b
a = a ^ b

print(f"After swap:  a = {a}, b = {b}")