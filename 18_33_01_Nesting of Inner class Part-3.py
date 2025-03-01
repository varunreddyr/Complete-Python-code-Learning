# Inner class nesting methods demo program

# Defining the Outer class 'Person'
class Person:
    def __init__(self, name, dd, mm, yyyy):
        print("Person Object creation...")  # Message indicating that a Person object is created
        self.name = name  # Assigning the name to the instance variable
        self.dob = self.Dob(dd, mm, yyyy)  # Creating an instance of the Inner class 'Dob'

    def info(self):
        """ Method to display person details along with Date of Birth """
        print('Name:', self.name)  # Prints the Person's name
        self.dob.display()  # Calls the display() method of the Inner class 'Dob'

    # Defining an Inner class 'Dob' inside 'Person'
    class Dob:
        def __init__(self, dd, mm, yyyy):
            print('Dob object is created.....')  # Message indicating that a Dob object is created
            self.dd = dd  # Day of birth
            self.mm = mm  # Month of birth
            self.yyyy = yyyy  # Year of birth

        def display(self):
            """ Method to display the Date of Birth """
            print('DoB={}/{}/{}'.format(self.dd, self.mm, self.yyyy))  # Prints the formatted Date of Birth

# Creating an instance of the Person class
p = Person('Varun Reddy', 24, 8, 1947)

# Calling the info() method to display details
p.info()

