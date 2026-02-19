# Reverse list without builtin functions 

# From Online 

list1 = [int(x) for x in input("Enter numbers with space: ").split()]

# 1. Find length manually (instead of using len())
count = 0
for i in list1:
    count += 1

# 2. Swap elements manually
start = 0
end = count - 1

while start < end:
    # Manual swap without any function
    temp = list1[start]
    list1[start] = list1[end]
    list1[end] = temp
    
    start += 1
    end -= 1

print("Reversed list:", list1)