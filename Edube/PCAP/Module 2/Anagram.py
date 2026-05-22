str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

a = sorted(str1)
b = sorted(str2)

if a == b:
    print("Anagrams")
else:
    print("Not Anagrams")