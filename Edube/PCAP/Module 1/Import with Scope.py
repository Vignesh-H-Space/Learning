import math

x = 100

def change():
    global x
    
    x = x + int(math.sqrt(2500))
    
    print("Inside change:", x)

def local_scope():
    x = 999
    
    print("Local x:", x)

print("Before:", x)

change()

local_scope()

print("After:", x)

print("Pi value:", round(math.pi, 2))