#How to access the static variables
#1. Inside Constructor by using self or classname
#2. Inside instance method by using self or class name.
#3. Inside classmethod by using cls or classname.
#4. Inside static method by using classname.
#5. outside of the class either by object reference or by class name

class Test:
    a=10        #1.Inside the class

    def __init__(self):
        print(self.a) #1.Inside the constructor by using self & classname.
        print(Test.a)
    def m1(self):
        print(self.a)  #2. Inside instance method by using self or class name.

    @classmethod
    def m2(cls):        #3.inside classmethod by using cls or classname.
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():          #4. Inside static method by using classname.
        print(Test.a)

t=Test()
print(t.a)            #5.Outside the class either by object reference or by class name
t.m1()
Test.m2()
Test.m3()



