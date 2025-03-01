# IS-A Relationship in Python (Inheritance)
# The IS-A relationship in Python represents inheritance,
# where a subclass inherits properties and behaviors (methods)
# from a parent (super) class. This means the subclass "IS-A" type of the superclass.
from collections import UserString

# Key Points About IS-A Relationship:
# ✔ Represents inheritance (i.e., one class derives from another).
# ✔ The child (subclass) gets all attributes and methods of the parent (superclass).
# ✔ Allows code reusability and hierarchical classification.
# ✔ Implemented using the class Subclass(Superclass) syntax in Python.
# Two uses of Inheritance:
# 1.Code Reusability.
# 2.Extendability.

# Defining the Parent class (Superclass)
class P:
    def m1(self):
        """
        Method m1() belongs to the Parent class.
        This method prints a message indicating it is a Parent method.
        """
        print('Parent Method')

# Defining the Child class (Subclass) which inherits from Parent class P
class C(P):
    def m2(self):
        """
        Method m2() belongs to the Child class.
        This method prints a message indicating it is a Child method.
        """
        print('Child Method')

# Creating an object of the Child class C
c = C()

# Calling the method from the Parent class (inherited by Child class)
c.m1()  # This will call the m1() method from class P

# Calling the method from the Child class
c.m2()  # This will call the m2() method from class C


