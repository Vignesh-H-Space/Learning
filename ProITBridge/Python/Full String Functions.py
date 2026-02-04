### String Functions 

#### Capitalize - Only the first letter of entire string and convert others letters into lower
string1 = "caPTain America"
string1 = string1.capitalize() 
print (string1)

string2 = "IrON Man"
string2 = string2.capitalize() 
print (string2)

#### Casefold - Return entire string in one format for caseless comparison
string3 = "caPTAIN AMERICA"
string3 = string3.casefold() 
print (string3)

string4 = "Marvel"
string4 = string4.casefold()
print(string4)

#### Count - Case Sensitive & Case Specific 
string5 = "caPTAIN AMERICA"
string5 = string5.count('a') 
print (string5)

string6 = "Doctor Strange"
string6 = string6.count('r') 
print (string6)

#### Center - Center the String (If the string or length is odd, then more space after string 
string7 = "cat"
string8 = "cat"
string7 = string7.center(4,"*") 
string8 = string8.center(4) 
print (string7+string1)
print (string8+string1)

#### Find - Returns lowest index of starting substring from the main string, returns -1 when not found 
string9 = "Umbrella"
string9 = string9.find("ll")
print(string9)

string10 = "Movie"
string10 = string10.find ("ae")
print(string10)


#### Index - Returns lowest index of starting substring from the main string, returns ValueError when not found 
string9 = "Umbrella"
string9 = string9.index("ll")
print(string9)

string10 = "Movie"
string10 = string10.index("e")
print(string10)

