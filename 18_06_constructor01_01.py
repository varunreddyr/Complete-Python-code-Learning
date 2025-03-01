# constructor is special method executed once the method is called

class Test:
    def __init__(self):
        print('constuctor is execute')
ti=Test()       # Constructor is executed when the object is created
t2=Test()       #Constuctor is useful for initialization of instance variable
t3=Test()
