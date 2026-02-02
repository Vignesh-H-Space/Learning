#  String Functions 

string1 = "caPTain America"
string1 = string1.capitalize() # Capitalize - Only the first letter of entire string and convert others letters into lower
print (string1)

string2 = "caPTAIN AMERICA"
string2 = string2.casefold() # Casefold - Return entire string in one format for caseless comparison
print (string2)

string3 = "caPTAIN AMERICA"
string3 = string3.count('a') # Count - Case Sensitive & Case Specific 
print (string3)

string4 = "cat"
string5 = "cat"
string5 = string4.center(4,"*") 
string4 = string4.center(4) # Center - Center the String (If the string or length is odd, then more space after string 
print (string4+string1)
print (string5+string1)

string6 = "caPTAIN AMERICA"
string6 = string6.count('a') # Count - Case Sensitive & Case Specific 
print (string6)

