# HAS-A Relationship Example:
# In this example, an Employee "HAS-A" Car. This demonstrates composition,
# where an Employee object contains a reference to a Car object.

# Defining the Car class
class Car:
    def __init__(self, name, model, color):
        """
        Constructor for Car class.
        :param name: Name of the car (e.g., 'Range Rover')
        :param model: Model of the car (e.g., 'Hybrid')
        :param color: Color of the car (e.g., 'White')
        """
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        """
        Method to display car information.
        """
        print('Car: {}, Model: {}, Color: {}'.format(self.name, self.model, self.color))


# Defining the Employee class
class Employee:
    def __init__(self, ename, eno, car):
        """
        Constructor for Employee class.
        :param ename: Employee name
        :param eno: Employee number
        :param car: Car object associated with the employee (HAS-A relationship)
        """
        self.ename = ename
        self.eno = eno
        self.car = car  # Employee has a Car object

    def getEmployee(self):
        """
        Method to display employee details along with their car information.
        """
        print('Employee Name:', self.ename)
        print('Employee No:', self.eno)
        print('Employee Car Info:')
        self.car.getinfo()  # Calling Car class method to display car details


# Creating a Car object
car = Car('Range Rover', 'Hybrid', 'White')

# Creating an Employee object and associating it with the Car object
emp = Employee('Varun Reddy', 20137441, car)

# Displaying Employee details along with Car details
emp.getEmployee()
