# Has-A vs Is-A:

# Has-A:When we want to extend one class functionality by using another class
#Is-A:When we want to use existing functionality but not to extend
# Employee Is-A Person
# Employee Has-A Car

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    def getinfo(self):
        print("\t Car Name:{} \n\t Model:{} \n\t Color:{}".format(self.name,self.model,self.color))
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
            print('Eat Biryani and Drink Beer')
class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.eno)
        print("Employee Salary:", self.esal)
        print("Employee Car Info:")
        self.car.getinfo()
c = Car("Innova", "2.5V", "Grey")
e = Employee('Durga', 48, 100, 10000, c)
e.eatndrink()
e.work()
e.empinfo()

# Output:
# Eat Biryani and Drink Beer
# Coding Python is very easy just like drinking Chilled Beer
# Employee Name: Durga
# Employee Age: 48
# Employee Number: 100
# Employee Salary: 10000
# Employee Car Info:
# 	 Car Name:Innova
# 	 Model:2.5V
# 	 Color:Grey