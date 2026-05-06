contacts = {
    "Alice": "555-0100",
    "Bob": "555-0200",
    "Mom": "555-9999"
}

# 1. Just the Names
print(contacts.keys()) 
# Output: dict_keys(['Alice', 'Bob', 'Mom'])

# 2. Just the Numbers
print(contacts.values())
# Output: dict_values(['555-0100', '555-0200', '555-9999'])

# 3. The Complete Contact Cards (Pairs)
print(contacts.items())
# Output: dict_items([('Alice', '555-0100'), ('Bob', '555-0200'), ('Mom', '555-9999')])