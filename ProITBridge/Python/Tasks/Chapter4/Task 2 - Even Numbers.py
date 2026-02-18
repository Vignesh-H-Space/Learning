# Task - 2 : Even Numbers 

# Create a list of numbers and print only even numbers using for loop 

list1 = [int(x) for x in input("Enter numbers with space ").split()]

print (f"The list of numbers are : {list1}")
print("The even numbers present in the list are :",end = " ")
for val in list1:
    if val % 2 == 0 :
        print(val,end = " ")