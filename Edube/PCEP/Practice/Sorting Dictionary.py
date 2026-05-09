marks = {
    "Arun": 78,
    "Meena": 95,
    "Kiran": 82
}

sorted_marks = sorted(marks.items(), key=lambda x: x[1])

print(sorted_marks)