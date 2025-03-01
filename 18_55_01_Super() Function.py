#Super() Function:
# By using Super() function , we can call the parent class methods explicitly from child class.


# We can call parent class m1 method by using child class m2 method
# class P:
#     def m1(self):
#         print('Parent M1 method')
# class C(P):
#     def m2(self):
#         self.m1()   # By using this we can call parent method
#         print('Child M2 method')
# c=C()
# c.m2()

#---------------------------
# This program shows when ever the child class method is having the same method as
#        as parent class which leads to ambiguity error :
# class P:
#     def m1(self):
#         print('Parent M1 method')
# class C(P):
#     def m1(self):
#         self.m1()   # By using this we can call parent method
#         print('Child M2 method')
# c=C()
# c.m1()
#
# Output :: RecursionError: maximum recursion depth exceeded

#-------------------------------
# By using Super() function:

class P:
    def m1(self):
        print('Parent M1 method')
class C(P):
    def m1(self):
        super().m1()   # By using Super() we can call same name parent method
        print('Child M2 method')
c=C()
c.m1()



