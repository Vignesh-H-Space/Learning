''' 1.while loop 
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