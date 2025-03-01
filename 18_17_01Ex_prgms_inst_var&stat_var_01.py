class Test:
    a=10
    def m1(self):
        Test.a=888  #static variable modified by using Class name reference

t1=Test()
t1.m1()
print(Test.a) # Static variable -->888 You can modify the static variable by using self keyword in instance method
print(t1.a) # Instance variable -->888

