class Test:
    a=10
    def m1(self):
        self.a=888

t1=Test()
t1.m1()
print(Test.a) # Static variable -->10 You can't modify the static variable by using self keyword in instance method
print(t1.a) # Instance variable -->888

