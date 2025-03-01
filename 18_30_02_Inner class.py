# Defining the Outer class
class Outer:
    def __init__(self):
        print('Outer class object creation')  # This message is printed when an Outer class object is created.

    # Defining the Inner class inside the Outer class (Nested Class)
    class Inner:
        def __init__(self):
            print('Inner class object creation')  # This message is printed when an Inner class object is created.

        def m1(self):
            print('Inner class method')  # This method prints a message when called.

# Creating an instance of the Outer class
o = Outer()  # This triggers the __init__ method of Outer, printing "Outer class object creation"

# Creating an instance of the Inner class using the Outer class instance
i = o.Inner()  # This triggers the __init__ method of Inner, printing "Inner class object creation"

# Calling the method of the Inner class
i.m1()  # This calls the m1() method of Inner, printing "Inner class method"




