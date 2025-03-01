class P:
    a=10
    def __init__(self):
        print('Parent Constructor')
        self.b=20
    def m1(self):
        print("Parent instance Method")
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    pass
c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
