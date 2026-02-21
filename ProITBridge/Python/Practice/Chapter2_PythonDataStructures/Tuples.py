# Tuples in Python

tuple1 = ()  # Empty Tuple
print(tuple1)

print(type(tuple1))


items_to_buy2 = ("Apple","Pomogranate","Orange","Apple",12,78,91.1)
print(items_to_buy2)

print(len(items_to_buy2))

print(type(items_to_buy2))

print(items_to_buy2[3]) # indexing

print(items_to_buy2[-4])   # negative indexing

print(items_to_buy2[0:3])  # slicing  

print(items_to_buy2[:3])  # slicing  

print(items_to_buy2[3:6])  # slicing  

# Returns empty tuple because slicing goes from left to right only
print(items_to_buy2[-2:-5])  # negative slicing 

print(items_to_buy2[-4:-1])  # negative slicing 

# items_to_buy2[3] = "Wow"  ERROR - Tuple is immutable