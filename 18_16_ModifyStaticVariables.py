# Modifying static variable
# We can modify static variable anywhere  by using the class name
# Note: We cannot modify static variable value by using self or object reference


class Test:
    a=10        #1.Inside the class

    def __init__(self):
        Test.a =20      #1.Modify Inside the constructor by using class name
        print(Test.a)
    def m1(self):
        Test.a=30 #2. Inside instance method by using self or class name.
        print(Test.a)

    @classmethod
    def m2(cls):        #3.inside class method by using cls or class name.
        cls.a =40
        Test.a=50
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():          #4. Inside static method by using class name.
        Test.a=60
        print(Test.a)
Test.a =70
t=Test()
print(t.a)            #5.Outside the class either by object reference or by class name
t.m1()
Test.m2()
Test.m3()