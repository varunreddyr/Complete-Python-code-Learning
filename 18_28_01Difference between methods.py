# Difference between Methods:
# Instance method and static method we can declare in same way

class Test:
    def m1(x):
        print("The value of x is:",x)

t=Test() #--> If you call this method by using object reference then this is called Instance method
t.m1() #-->This method is not executed because x is considered as self,We didnt provide 2 arguments.
Test.m1(20)   #--> If you call this method by using Class reference then this is called Static method

