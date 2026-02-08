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


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
items_to_buy.extend("Banana") # extend --The string gets appended as iteral 
print(items_to_buy) 


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
print(items_to_buy.index("Apple")) # Index - Returns the index, returns only first index if duplicate exists
# print(items_to_buy.index("Asad")) # ERROR - Since element not present in list 


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
items_to_buy.insert(3,"Mango") # Insert - Insert the element at the index specified
items_to_buy.insert(-3,"Kiwi") # Can even insert at the end 
items_to_buy.insert(32,"Watermelon") # If Index is too large, it gets appended at the end
print(items_to_buy) 


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
items_to_buy.pop() # Pop - Removes the last element of the list
print(items_to_buy) 


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
items_to_buy.remove("Apple")  # Remove - Removes the first occurence of the element
# items_to_buy.remove("Apda")  ERROR - Cant remove if the element doesnt exist
print(items_to_buy) 


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
items_to_buy.reverse() # Reverse - Reverses the list elements
print(items_to_buy) 


items_to_buy = ["Apple","Pomogranate","Orange","Apple",12,78,91.1]
# items_to_buy.sort() ERROR - Since sorting cant happen with different datatypes
items_to_buy2 = ["Apple","Pomogranate","Orange","Apple"]
items_to_buy2.sort() 
print(items_to_buy2) 
