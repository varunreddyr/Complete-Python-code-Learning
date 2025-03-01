class Test:
    a=10
    def __init__(self):
        self.b=20

t1=Test()
t2=Test()
print("t1:",t1.a,t1.b) #t1: 10 20
print("t2:",t2.a,t2.b) #t2: 10 20
Test.a=888
Test.b=999
print("t1:",t1.a,t1.b) #t1: 888 20
print("t2:",t2.a,t2.b) #t2: 888 20
print("Test:",Test.a,Test.b) #Test: 888 999
