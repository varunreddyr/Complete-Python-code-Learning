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
            @staticmethod
            def m1(): #m1() is static method so we don't need to create InnerInner() object Instead we can directly call from InnerInner class

                    print('Nested static Inner class method')  # This method prints a message when called.



#Shortcut:
Outer().Inner().InnerInner.m1()

# The above m1() is static method so we don't need to create InnerInner() object Instead we can directly call from InnerInner class




