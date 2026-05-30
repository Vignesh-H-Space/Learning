class NegativeAgeError(Exception):
    pass

try:
    age = int(input("Age: "))

    if age < 0:
        raise NegativeAgeError("Age cannot be negative")

    print("Age accepted")
