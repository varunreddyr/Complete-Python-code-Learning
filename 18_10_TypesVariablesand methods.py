#Instance Variables
# If the values of the variables varies from object to object then it is called Instance variable
# For every object separate copy of variables created.

#Static variables:
#If the value of the variables does not vary from object to object.
#This can be created at class level.

#Local variable
#The variables declared inside the methods to meet temporary requirements.


class student:
    school_name = 'Durgasoft'   #static variable

    def __init__(self,name,rollno):
        self.name = name       #Instance variables
        self.rollno = rollno   #Instance variable

    def info(self):
        x=10                   #Local variables
        for i in range(x):
            print(i)
