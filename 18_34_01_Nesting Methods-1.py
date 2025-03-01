# Nested Methods:
# We can declare methods inside a method , such type of methods are called Nested methods
#If you want to rewrite the code every time , then Nested method are used.

# Example of Nested Methods in Python

class Calculator:
    def __init__(self, num1, num2):
        """ Constructor to initialize two numbers """
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        """ Outer method to perform calculations """

        def add():
            """ Inner method to perform addition """
            return self.num1 + self.num2

        def subtract():
            """ Inner method to perform subtraction """
            return self.num1 - self.num2

        def multiply():
            """ Inner method to perform multiplication """
            return self.num1 * self.num2

        def divide():
            """ Inner method to perform division (with zero check) """
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Division by zero is not allowed"

        # Calling inner functions and returning results
        return {
            "Addition": add(),
            "Subtraction": subtract(),
            "Multiplication": multiply(),
            "Division": divide()
        }


# Creating an instance of Calculator
calc = Calculator(10, 5)

# Calling the outer method which internally calls nested methods
results = calc.calculate()

# Displaying the results
for operation, result in results.items():
    print(f"{operation}: {result}")
