class Test:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999

t1=Test()
t2=Test()
t1.m1()
t2.m1()
print("t1:",t1.a,t1.b) #t1: 888 20
print("t2:",t2.a,t2.b) #t2: 888 20
print("Test:",Test.a,Test.b) #Test: 888 999

