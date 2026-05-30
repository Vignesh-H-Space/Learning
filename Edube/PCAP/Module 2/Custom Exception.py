class NegativeAgeError(Exception):
    pass

try:
    age = int(input("Age: "))
