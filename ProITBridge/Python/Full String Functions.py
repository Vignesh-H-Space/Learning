### String Functions - Each function with 2 examples

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

#### Upper - Converts all the characters to upper case 
word1 = "Multiplex"
print(word1.upper()) 

word2 = "Doctor Strange"
print(word2.upper())

#### Lower - Converts all the characters to lower case 
word1 = "MULTIPLEX"
print(word1.lower()) 

word2 = "Doctor Strange"
print(word2.lower())

#### Title - Converts the first letter of every word to uppercase 
word1 = "avengers infinity WAR"
print(word1.title()) 

word2 = "THOR ragnarok"
print(word2.title())

#### Swapcase - Swaps all the cases of all letters, i.e., Lower letters becomes upper and upper letters becomes lower. 
word1 = "avengers infinity WAR"
print(word1.swapcase()) 

word2 = "THOR ragnarok"
print(word2.swapcase())

#### Startswith - Returns true when the string starts with else returns false 
word1 = "avengers infinity WAR"
print(word1.startswith("av")) 

word2 = "THOR ragnarok"
print(word2.startswith("ok"))

#### Endswith - Returns true when the string ends with else returns false 
word1 = "avengers infinity WAR"
print(word1.endswith("ar")) 

word2 = "THOR ragnarok"
print(word2.endswith("ok"))

#### Replace - Replaces a substring with another substring 
word1 = "avengers infinity WAR"
print(word1.replace("infinity","Star")) 

word2 = "THOR ragnarok"
print(word2.replace("ragnarok","Thunder"))

#### Split - Split the string into list 
word1 = "avengers infinity WAR"
print(word1.split()) 

word2 = "THOR ragnarok"
print(word2.split())

#### Join - Joins the list into a single string with given 
word1 = ["Avengers", "End", "Game"]
print(" ".join(word1)) 

word2 = ["03", "02", "2026"]
print("-".join(word2))

#### isalnum - returns true if string is alpha numeric else false
s = "Mango121"
print(s.isalnum())

s = "Mango/121"
print(s.isalnum())

#### isalpha - returns true if string is alpha else false
s = "Mango"
print(s.isalpha())

s = "Mango121"
print(s.isalpha())

#### isdecimal - returns true if string is decimal else false
s = "202.64"
print(s.isdecimal())

s = "121"
print(s.isdecimal())

#### isdigit - returns true if string is digit else false
s = "202.64"
print(s.isdigit())

s = "121"
print(s.isdigit())

#### Islower - returns true if entire string is lower else false 
word1 = "avengers infinity WAR"
print(word1.islower()) 

word2 = "thor ragnarok"
print(word2.islower())

#### Isupper - returns true if entire string is upper else false 
word1 = "avengers infinity WAR"
print(word1.isupper()) 

word2 = "THOR"
print(word2.isupper())

#### lstrip - remove space in left 
word1 = "        avengers infinity WAR   "
print(word1.lstrip()) 

word2 = "       THOR  "
print(word2.lstrip()) 

#### rstrip - remove space in right 
word1 = "        avengers infinity WAR     "
print(word1.rstrip()) 

word2 = "       THOR    "
print(word2.rstrip()) 

#### strip - remove space in left and right 
word1 = "        avengers infinity WAR     "
print(word1.strip()) 

word2 = "       THOR    "
print(word2.strip()) 