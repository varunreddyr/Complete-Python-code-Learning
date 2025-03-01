# Class Methods
# For every class , Python will create a class object

class Test:
    x=10
    @classmethod
    def info(cls):
        print(cls.x)
t=Test()
t.info()