# How to use members of one class in another class
# 1.By Has-A relationship(Composition) -->Code Reusability
# 2.By Is-A relationship(inheritance)  -->

# Example for Has-A relationship

class Engine:
    def useEngine(self):
        print('Engine specific Functionality')
class Car:
    def __init__(self):
        self.engine=Engine()
    def useCar(self):
        print('Car required Engine Functionality')
        self.engine.useEngine()

c=Car()
c.useCar()
