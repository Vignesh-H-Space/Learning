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


# Tuple Functions 

items_to_buy = ("Apple","Pomogranate","Orange","Apple",12,78,91.1)
print(items_to_buy.count("Apple"))  # Count - Count the number of occurences of the element in tuple 


items_to_buy = ("Apple","Pomogranate","Orange","Apple",12,78,91.1)
print(items_to_buy.index("Apple"))  # Index - Returns the index, returns only first index if duplicate exists


# Set functions 

items_to_buy = set(("Apple","Pomogranate","Orange","Apple",12,78,91.1))

items_to_buy.add("Banana")   # Add - Adds element to set (no duplicates allowed)
print(items_to_buy)

items_to_buy.remove("Apple")  # Remove - Removes specified element (Error if element not found)
print(items_to_buy)

# items_to_buy.remove("Mango")  # ERROR - Element not present

items_to_buy.discard("Orange")  # Discard - Removes element if present (No error if not found)
print(items_to_buy)

items_to_buy.pop()  # Pop - Removes a random element from the set
print(items_to_buy)

items_to_buy.clear()  # Clear - Removes all elements from the set
print(items_to_buy)


# Dictionary Functions


student = {
    "name": "Asad",
    "age": 21,
    "course": "Python"
}

print(student.get("name"))   # Get - Returns value of the key
print(student.get("marks"))   # Returns None if key doesn't exist

student["age"] = 22  # Update value using key
print(student)

student.update({"marks": 95})  # Update - Adds new key-value pair
print(student)

print(student.keys())  # Keys - Returns all keys

print(student.values())  # Values - Returns all values

print(student.items())  # Items - Returns key-value pairs as tuples

student.pop("course")  # Pop - Removes specified key
print(student)

student.popitem()  # Popitem - Removes last inserted key-value pair
print(student)

student.clear()  # Clear - Removes all elements from dictionary
print(student)