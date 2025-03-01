#local variables:
#Local variables are particular to that method only.
class Test:
    @staticmethod
    def average(list1):
        result=sum(list1)/len(list1) #Here "result" is the local variable
        print("The average of numbers:",result)

    @staticmethod
    def wish(name):
        for i in range(10): #Here "i" is the local variable
            print('Good eveng:',i+1,name)
list1=[20,30,40]
Test.average(list1)
Test.wish("varun")