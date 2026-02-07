# List in Python

list1 = []  # Empty List
print(list1)

print(type(list1))


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
print(items_to_buy)

print(len(items_to_buy))

print(type(items_to_buy))

print(items_to_buy[3]) # indexing

print(items_to_buy[-4])   # negative indexing

print(items_to_buy[0:3])  # slicing  

print(items_to_buy[:3])  # slicing  

print(items_to_buy[3:6])  # slicing  

# Returns empty list because slicing goes from left to right only
print(items_to_buy[-2:-5])  # negative slicing 

print(items_to_buy[-4:-1])  # negative slicing 

