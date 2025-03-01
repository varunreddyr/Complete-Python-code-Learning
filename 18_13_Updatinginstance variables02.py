#You can Update the instance variables

class test:
    def __init__(self):
        self.a = 10 #1.Instance variables
        self.b = 20


t=test()
t.a=888
t.b=999
t1=test()
print(t.a,t.b) #Result : 888 999
print(t1.a,t1.b) #Result : 10 20


