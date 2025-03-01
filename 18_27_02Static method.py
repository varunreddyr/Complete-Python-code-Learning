#Static method

class Maths:
    '''Maths calculator'''
    @staticmethod
    def add(a,b):
        print('The sum:',(a+b))
    @staticmethod
    def product(a,b):
        print("The product of numbers:",(a*b))
    @staticmethod
    def average(a,b):
        print("The average of the numbers:",(a+b)/2)
Maths.add(10,20)
Maths.product(20,30)
Maths.average(30,40)

