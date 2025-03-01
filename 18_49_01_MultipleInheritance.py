# 4.Multiple Inheritance:
# Multiple Inheritance is when a child class (subclass) inherits from more than one parent class (superclass).
# This allows the child class to access attributes and methods from multiple parent classes.

class P1:
    def m1(self):
        print('Parent1 Method')
class P2():
    def m1(self):
        print('Parent2 Method')
class C(P1,P2):
    def m3(self):
        print('Child Method')
c=C()
c.m1()
c.m2()
c.m3()


# If the same method is inherited from both parent classes, then Python will always consider the order of Parent classes in the declaration of the class
# class C(P1,P2) ----> P1 method is considered.
# class C(P2,P1) ----> P2 method is considered.