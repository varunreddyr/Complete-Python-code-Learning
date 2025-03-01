class Test:
    a = 10
    def __init__(self):
        Test.b = 20
        del Test.a

    def m1(self):
        Test.c = 30
        del Test.b

    @classmethod
    def m2(cls):
        cls.d = 40
        del Test.c

    @staticmethod
    def m3():
        Test.e = 50
        del Test.d

t=Test()
print(Test.__dict__) #b=20

t.m1()
print(Test.__dict__) #c=30

t.m2()
print(Test.__dict__) #d=40

t.m3()
print(Test.__dict__) #e=50

del Test.e
print(Test.__dict__) #all variables are deleted

#Note:Static variable you cant use the reference variable only you have to use cls or classname