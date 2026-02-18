# Task 3 - Division by Zero

# A program which handles Division by zero using try-except
print("Program to Divide two numbers")
num1 = int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))
try :
    print(num1/num2)
except ZeroDivisionError:       # Exception catch
    print("Error, Cannot divide by Zero")