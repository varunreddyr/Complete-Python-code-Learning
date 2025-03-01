#Various places usage of instance variable
#1. Inside constructor by using self
#2.Inside Instance method by using self
#3.Outside the class by using object reference variable.
class test:


    def __init__(self):
        self.a = 10 #1.Instance variables
        self.b = 20
    def m1(self):
        self.c =30 #2.Instance variable ,but inside the method.

t1=test()
t1.m1()
t1.d=40 #3.Outside the class by using object reference variable.
t2=test()
print("t1 dict:",t1.__dict__)    #Result :{'a': 10, 'b': 20, 'c': 30, 'd': 40}
print("t2 dict:",t2.__dict__)    #Result: t2 dict: {'a': 10, 'b': 20}
