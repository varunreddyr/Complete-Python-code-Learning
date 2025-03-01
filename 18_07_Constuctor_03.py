#This is method overloading because of two methods, Python does not support method overloading .
#It always considers they latest method , In this second method is considered
class test:
    def __init__(self):  #This one is not initialized
        print("no-arg constructor")

    def __init__(self, x):  # This one is latest constructor and initialized.
        print("one-arg constructor")


t1 = test()  # Error because it always expect one argument
t2 = test(10)  # This one executes when we comment above line
