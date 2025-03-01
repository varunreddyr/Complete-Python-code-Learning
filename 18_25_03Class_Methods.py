# Class Methods
# Program to track the number of objects created for a class:

class Test:
    """
    A class to track the number of objects created.
    """
    count = 0  # Class variable to keep track of object count

    def __init__(self):
        """
        Constructor that increments the object count each time an object is created.
        """
        Test.count = Test.count + 1

    @classmethod
    def get_no_of_objects(cls):
        """
        Class method to display the number of objects created.
        """
        print("The number of objects created:", cls.count)

# Calling the class method before creating any objects
Test.get_no_of_objects()  # Output: The number of objects created: 0

# Creating objects
t1 = Test()
t2 = Test()
t3 = Test()

# Calling the class method after creating objects
Test.get_no_of_objects()  # Output: The number of objects created: 3