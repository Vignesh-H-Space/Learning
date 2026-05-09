student = {
    "name": "Arun",
    "marks": {
        "math": 90,
        "science": 80
    }
}

copy_student = student.copy()

copy_student["marks"]["math"] = 100

print(student)