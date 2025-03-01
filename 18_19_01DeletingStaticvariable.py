class Test:
    a=10
    @classmethod
    def m1(cls):
        del Test.a
        #del cls.a      You can also use this method.

#del Test.a       You can also use class name
Test.m1()
print(Test.__dict__)  # a is deleted

