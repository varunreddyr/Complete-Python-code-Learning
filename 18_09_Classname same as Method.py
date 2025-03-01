# We can use class name same as Method name , but it is not advisable

class test:
    def test(self):
        print("This is special method ")
t=test() # Constructor is executed
t.test() # test() method is executed