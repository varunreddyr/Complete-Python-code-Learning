# Defining the Outer class
class Outer:
    def __init__(self):
        print('Outer class object creation')  # This message is printed when an Outer class object is created.

    # Defining the Inner class inside the Outer class (Nested Class)
    class Inner:
        def __init__(self):
            print('Inner class object creation')  # This message is printed when an Inner class object is created.

        class InnerInner:
            def __init__(self):
                print('Inner Inner class object creation')
            def m1(self):
                    print('Nested Inner class method')  # This method prints a message when called.


o=Outer()
i=o.Inner()
ii=i.InnerInner()
ii.m1()

#Shortcut:
Outer().Inner().InnerInner().m1()




