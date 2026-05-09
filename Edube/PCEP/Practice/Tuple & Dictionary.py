students = (
    ("Vignesh", "Python"),
    ("Rahul", "Java"),
    ("Anu", "Python"),
    ("Kiran", "C"),
    ("Meena", "Java"),
    ("Arun", "Python")
)

course_count = {}

for name, course in students:
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1

print(course_count)