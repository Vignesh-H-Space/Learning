students = {
    101: {"name": "Arun", "marks": (67, 88, 91)},
    102: {"name": "Meena", "marks": (90, 91, 92)},
    103: {"name": "Kiran", "marks": (70, 60, 65)}
}

topper = ""
highest_total = 0

for roll, details in students.items():
    total = sum(details["marks"])

    if total > highest_total:
        highest_total = total
        topper = details["name"]

print(topper)
print(highest_total)