# Set in Python 


set1 = set()  # Empty Set
print(set1)

print(type(set1))

# Set allows only one argument and it must be iterable like list, tuple or string

# Two different ways to declare sets

items_to_buy1 = set(("Apple","Pomogranate","Orange","Apple",12,78,91.1)) 

items_to_buy2 = {"Apple","Pomogranate","Orange","Apple",12,78,91.1}

# The order changes everytime 
print(items_to_buy2) 

print(items_to_buy1) # Duplicate is not allowed and also auto indexing 

# print(items_to_buy1[0]) - ERROR - set doesnt allow indexing and slicing 

print(len(items_to_buy1))

print(type(items_to_buy1)) 

