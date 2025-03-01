#Instance Method
#The methods in which instance variables are declared.
#Accesing the instance variables then the method is called Instance method.

#Class Method:
#The methods in which static variables are used.
#when we are using class method we have to use @classmethod operator

#Static methods
#General utility methods are called static methods.
#Static methods should be declared by using @staticmethod decorator


class student:
    school_name = 'Durgasoft'  #static variable

    def __init__(self, name, rollno):
        self.name = name  #Instance variables
        self.rollno = rollno  #Instance variable

    def info(self):
        x = 10  #Local variables
        for i in range(x):
            print(i)

    def getStudentInfo(self):  #Instance method
        print("Student name:", self.name)
        print("Student rolln0:", self.rollno)

    @getStudentInfo       # This is class method operator
    def getSchoolInfo(cls):  #Class Method , cls is the reference variable for class object.
        print("School Name:", cls.school_name)

    @staticmethod       #@Staticmethod operator
    def getSum(a,b):    #Static method.
        return a+b


