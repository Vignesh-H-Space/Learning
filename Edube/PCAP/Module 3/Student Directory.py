class Student:

    total = 0

    def __init__(self, name):
        self.name = name
        self.marks = []
        Student.total += 1
