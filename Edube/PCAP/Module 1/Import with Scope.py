x = 100

def change():
    global x
    x = x + 50
    print("Inside:", x)

print("Before:", x)

change()

print("After:", x)