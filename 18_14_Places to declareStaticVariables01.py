#Places to declare Static Variables
#1. within the class directly,but outside of any method or constructor
#2.Inside constructor by using class name
#3.Inside Instance method by using classname
#3.Inside class method by defining cls or classname
#5.Inside static method by using classname
#6.From outside of the class by using class name
class Test:
    a=10        #1.Inside the class

    def __init__(self):
        Test.b =20 #2.Inside the constructor by using class name

    def m1():
        Test.c=30 #3.Inside Instance method by using classname
    @classmethod
    def m2(cls):
        cls.d = 40 #4. Inside the class method by using cls
        Test.e =50
    @staticmethod
    def m3():    #5. Inside static method by using classname
        Test.f = 60
Test.g = 70      #6.From outside of the class by using class name
print(Test.__dict__)

