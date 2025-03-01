# Class Methods
# For every class , Python will create a class object

class Bird:
    """
    A class to represent birds with a class attribute for wings.
    """
    wings = 2  # Class attribute representing the number of wings

    @classmethod
    def fly(cls, name):
        """
        Class method to simulate a bird flying.

        Parameters:
        name (str): The name of the bird.
        """
        print('{} flying with {} wings'.format(name, cls.wings))


# Calling the class method without creating an instance
Bird.fly('Parrot')  # Output: Parrot flying with 2 wings
Bird.fly('Eagle')  # Output: Eagle flying with 2 wings