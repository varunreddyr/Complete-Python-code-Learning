# 🔹 mro() in Python (Method Resolution Order)
# 🔹 mro() (Method Resolution Order) determines the order in which Python searches
#    for a method in a class hierarchy (especially in multiple and hybrid inheritance).
# 🔹 It follows the C3 Linearization (Depth-First, Left-to-Right) algorithm.
# 🔹 Helps in resolving method conflicts in multiple inheritance.
from pydoc import classify_class_attrs

# syntax:print(classname.mro())
#  objectclass
#
#      class A:
#
#
# classB:    class C:
#
#
#     classD:

# mro(A)=A,object
# mro(B)=B,A,object
# mro(C)=C,A,object
# mro(D)=D,B,C,object



class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(A):
    def m1(self):
        print('C class method')
class D(B,C): #
    def m1(self):
        print('D class method')

d=D()
d.m1()
print(D.mro())





