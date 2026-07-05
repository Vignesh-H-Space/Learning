class Student:

    total = 0

    def __init__(self, name):
        self.name = name
        self.marks = []
        Student.total += 1
        
    def add(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(self.name)
        print(self.marks)
        print(self.average())
