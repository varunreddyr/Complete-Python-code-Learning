#Super() Function:
# By using Super() function , we can call the parent class methods explicitly from child class.

class P:
    a=10
    def __init__(self):
        print('Parent constructor')

    def m1(self):
        print('Parent Instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    def __init__(self):
        print('Child Method')
    def method1(self):
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        super().__init__()

c=C()
c.method1()

# Output:
# Child Method
# 10
# Parent Instance method
# Parent class method
# Parent static method
# Parent constructor
