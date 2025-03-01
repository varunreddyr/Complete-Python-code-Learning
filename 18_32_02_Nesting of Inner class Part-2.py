# Nesting of Inner Classes Demo Program

# Defining the Outer class 'Human'
class Human:
    def __init__(self, name):
        print('Human Object Creation.....')  # This message is printed when a Human object is created.
        self.name = name  # Assigning the name to the instance variable
        self.head = self.Head()  # Creating an instance of the Inner class 'Head'

    def info(self):
        """ Method to display human details and invoke methods from inner classes """
        print('Hello, My self', self.name)  # Prints the Human name
        self.head.talk()  # Calling the talk() method of the Head class
        self.head.brain.think()  # Calling the think() method of the Brain class inside Head

    # Defining an Inner class 'Head' inside 'Human'
    class Head:
        def __init__(self):
            print('Head Object creation')  # This message is printed when a Head object is created.
            self.brain = self.Brain()  # Creating an instance of the Inner class 'Brain' inside Head

        def talk(self):
            """ Method representing talking functionality of the Head """
            print('Talking....')

        # Defining another Inner class 'Brain' inside 'Head'
        class Brain:
            def think(self):
                """ Method representing thinking functionality of the Brain """
                print('Brain Object creation')  # This message is printed when the Brain object is accessed.
                print('Thinking....')

# Creating an instance of the Human class
human = Human('Varun Reddy')

# Calling the info() method to demonstrate functionality
human.info()
