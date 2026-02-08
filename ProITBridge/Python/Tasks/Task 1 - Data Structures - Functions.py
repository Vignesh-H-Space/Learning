# Data Structures 

# List, Tuple, Set, Dictionary - One example for each functions 


# List Functions

items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
items_to_buy.append("Watermelon")  # Append - Adds new element to the end of list 
print(items_to_buy)


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
items_to_buy.clear()  # Clear - Clears the entire list elements and only empty list appears 
print(items_to_buy)


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
items = items_to_buy.copy()  # Copy - Returns a shallow copy of list
items.clear()
print(items)
print(items_to_buy)


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
print(items_to_buy.count("Apple"))  # Count - Counts the total occurences of a particular element in list
print(items_to_buy.count("Apples")) # Returns 0 if the element doesn't exist

