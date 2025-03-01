# 3.Hierarchical Inheritance:
# Hierarchical Inheritance is when multiple child classes inherit from a single parent class.
# This allows different subclasses to share common functionality from the parent while also implementing their own unique behavior.
class P:
    def m1(self):
        print('Parent Method')
class C1(P):
    def m2(self):
        print('Child-1 Method')
class C2(P):
    def m3(self):
        print('Child-2 Method')
c1=C1()
c2=C2()
c1.m1()
c1.m2()

c2.m1()
c2.m3()
