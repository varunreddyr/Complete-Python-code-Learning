class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatdrink(self):
        print('Eat Biryani & Drink Beer')
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        # self.name=name
        # self.age=age  ---> This two vars are derived by using super().__init__(name,age)
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print('Coding Python Programs')
    def empInfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)

e=Employee('Varun',30,20137441,100000)
e.eatdrink()
e.work()
e.empInfo()