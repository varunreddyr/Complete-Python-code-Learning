class Test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=888
        self.b=999

t1=Test()
t2=Test()
t1.m1()
print("t1:",t1.a,t1.b) #t1: 888 999
print("t2:",t2.a,t2.b) #t2: 10 20

