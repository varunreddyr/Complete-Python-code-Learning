class Student:
    """
    A class to represent a student with name and marks attributes.
    """

    def set_name(self, name):
        """Sets the name of the student."""
        self.name = name

    def get_name(self):
        """Returns the name of the student."""
        return self.name

    def set_marks(self, marks):
        """Sets the marks of the student."""
        self.marks = marks

    def get_marks(self):
        """Returns the marks of the student."""
        return self.marks


# Get the number of students from user input
n = int(input('Enter number of students: '))
students = []  # List to store student objects

# Loop to take input for each student
for i in range(n):
    s = Student()  # Create a new Student object
    name = input('Enter Student name: ')  # Get student name
    s.set_name(name)  # Set the name for the student
    marks = int(input('Enter marks: '))  # Get student marks
    s.set_marks(marks)  # Set the marks for the student
    students.append(s)  # Add the student object to the list

# Display student details
for s in students:
    print('Hello', s.get_name())  # Print the student's name
    print('Your marks are:', s.get_marks())  # Print the student's marks
    print()  # Print a blank line for better readability
