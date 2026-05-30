try:
    a = float(input("First number: "))
    op = input("Operator (+ - * /): ")
    b = float(input("Second number: "))

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Invalid operator")

except ValueError:
    print("Please enter numbers only!")

except ZeroDivisionError:
    print("Cannot divide by zero!")