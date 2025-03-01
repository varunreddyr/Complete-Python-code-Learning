# Accessing members of one class inside another class

# Define the Employee class
class Employee:
    def __init__(self, eno, ename, esal):
        # Initializing employee details
        self.eno = eno  # Employee number
        self.ename = ename  # Employee name
        self.esal = esal  # Employee salary

    def display(self):
        # Method to display employee details
        print('Employee Number:', self.eno)
        print('Employee Name:', self.ename)
        print('Employee Salary:', self.esal)

# Define the Manager class
class Manager:
    @staticmethod  # Static method (does not require an instance of Manager)
    def updateEmployeeSal(emp):
        # Updating the employee salary
        emp.esal = emp.esal + 1000  # Adding 1000 to the employee's salary
        # Modifying employee name
        emp.ename = emp.ename + ' Reddy'
        # Display updated employee details
        emp.display()

# Creating an Employee object
emp = Employee(100, 'Varun', 40000)

# Calling the static method of Manager class to update employee details
Manager.updateEmployeeSal(emp)

