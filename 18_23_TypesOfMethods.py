# Three types of Methods

# 1. Instance Method
# 2. Class Method
# 3. Static Method

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Hi', self.name)
        print('Your marks are:', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('You got First Grade')
        elif self.marks >= 50:
            print('You got Second Grade')
        elif self.marks >= 35:
            print('You got Third Grade')
        else:
            print('You are Failed')

# Getting the number of students
n = int(input('Enter number of students: '))

for i in range(n):
    name = input('Enter student name: ')
    marks = int(input('Enter marks: '))  # Getting marks input before using it
    s = Student(name, marks)  # Passing name and marks to Student class
    s.display()
    s.grade()
    print()  # For better readability
