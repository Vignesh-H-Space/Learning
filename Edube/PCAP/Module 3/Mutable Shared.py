class Kennel:
    dogs = []  # Class Variable (Shared)

k1 = Kennel()
k2 = Kennel()

# Modifying the list using the first object
k1.dogs.append("Rex")

# Reassigning the list using the second object
k2.dogs = ["Max"]

print(k1.dogs)
print(k2.dogs)
print(Kennel.dogs)