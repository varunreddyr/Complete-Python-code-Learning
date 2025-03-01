# Three types of Methods

# 1. Instance Method
# 2. Class Method
# 3. Static Method

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return self.name, self.marks, self.grade()

    def grade(self):
        if self.marks >= 60:
            return 'First Grade'
        elif self.marks >= 50:
            return 'Second Grade'
        elif self.marks >= 35:
            return 'Third Grade'
        else:
            return 'Failed'

# Getting the number of students
n = int(input('Enter number of students: '))
students = []

for i in range(n):
    name = input('Enter student name: ')
    marks = int(input('Enter marks: '))  # Getting marks input before using it
    s = Student(name, marks)
    students.append(s.display())

# Displaying student data in an asterisk table
print("\n********** Student Results **********")
print("************************************")
print("* Name        * Marks *    Grade    *")
print("************************************")
for student in students:
    print(f"* {student[0]:<10} *  {student[1]:<5} * {student[2]:<10} *")
print("************************************")
