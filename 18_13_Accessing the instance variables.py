
class test:


    def __init__(self):
        self.a = 10 #1.Instance variables
        self.b = 20
    def m1(self):
        self.c =30 #2.Instance variable ,but inside the method.

t=test()
t.m1()
print(t.a) #Accessing the instance variable outside the class
print(t.b) #Accessing the instance variable outside the class
