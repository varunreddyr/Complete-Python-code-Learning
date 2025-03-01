# 2.Multi Level Inheritance:
# Multi-Level Inheritance is when a child class (subclass) inherits from a parent class (superclass), which itself inherits from another superclass.
# This forms a chain of inheritance, where a class inherits from another class, which in turn inherits from another class.
class P:
    def m1(self):
        print('Parent Method')
class C(P):
    def m2(self):
        print('Child Method')
class CC(C):
    def m3(self):
        print('Sub Child Method')
c=CC()
c.m1()
c.m2()
c.m3()
