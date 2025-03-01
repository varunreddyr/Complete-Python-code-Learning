#You can delete the instance variables
# syntax: del self.a
#syntax: del t.a  #outside the class
#syntax : del t.a, t.b
class test:



    def __init__(self):
        self.a = 10 #1.Instance variables
        self.b = 20
        self.c = 30
        self.d =40
    def m1(self):
        del self.c

t=test()
t.m1()
print(t.__dict__) #Result : {'a': 10, 'b': 20, 'd': 40}
t1=test()
del t1.b , t1.d
print(t1.__dict__) # Result:{'a': 10, 'c': 30}

