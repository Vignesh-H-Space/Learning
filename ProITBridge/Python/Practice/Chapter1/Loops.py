''' 
1.while loop 
2.for loop
3.if else
4.if elif else
5.user defined functions without for loop, if loop 
6.user defined functions with for loop 
7.user defined functions with for loop and if condition 
8.break
9.continue 
10.for loop with in operator
11.for loop with if statement
12.for loop with not in operator
13.if with in operator 
14.if with not in operator''' 

# while loop 1 
str1 = input("Enter a string: ")
length = len(str1)
while length > 0 : 
   print (str1) 
   str1 = str1[:-1] 
   length = len(str1) 

# while loop 2 
word = 'N'
while word.lower() != 'q' : 
  word = input("Enter q to quit and any other letter to continue: ") 

# For loop 1
str1 = input("Enter a string: ") 
length = len(str1) 
for i in range(0,length+1): 
  print (str1) 
  str1 = str1[:-1] 
  length = len(str1) 

# For loop 2 
for i in range(1, 100): 
  word = input("Enter q to quit and any other letter to continue: ")
  if word.lower() == 'q':
     break
 
 # if else 1
number = 2 
if number % 2 == 0 :
    print("Number is even")
else :
    print("Number is odd")

# if else 2
word = "IRON MAN"
if word.isupper() == True : 
    print("The word is in upper case ")
else :
    print ("The word is in lower case ")
    
# if elif 
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# User-defined function without for loop, if loop
def greet():
    print("Hello, welcome ")

greet()

# User-defined function with for loop
def print_numbers():
    for i in range(1, 6):
        print(i)

print_numbers()

# User-defined function with for loop and if condition
def even_numbers():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)

even_numbers()

# break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

# for loop with in operator
name = "PYTHON"

for letter in name:
    print(letter)

# for loop with if statement 
for i in range(1, 11):
    if i > 5:
        print(i)

# for loop with not in operator 
word = "python"

for letter in "aeiou":
    if letter not in word:
        print(letter, "not in word")

# if with in operator 
text = "learning python"

if "python" in text:
    print("Python found")
else:
    print("Python not found")

# if with not in operator 
username = "admin"

if "@" not in username:
    print("Invalid username")
else:
    print("Valid username")
