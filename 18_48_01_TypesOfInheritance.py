# 1.Single Inheritance
# 2.Multi Level Inheritance
# 3.Hierarchical Inheritance
# 4.Multiple Inheritance
# 5.Hybrid Inheritance
# 6.Cyclic Inheritance


# 1.Single Inheritance:
# Single Inheritance is when a child class (subclass) inherits from a single parent class (superclass).
# The child class gets all the attributes and methods of the parent class and can also override or extend them.

class P:
    def m1(self):
        print('Parent Method')
class C(P):
    def m2(self):
        print('Child Method')
c=C()
c.m1()
c.m2()
