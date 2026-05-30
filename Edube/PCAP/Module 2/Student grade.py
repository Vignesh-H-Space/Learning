grades = {}

for _ in range(3):
    name = input("Student name: ")
    mark = int(input("Mark: "))
    grades[name] = mark

top_student = max(grades, key=grades.get)

print("Top Student:", top_student)
print("Mark:", grades[top_student])