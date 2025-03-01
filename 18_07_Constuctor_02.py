#Constuctor is not necessary , Phyton will provide default constructor

class test:
  def __init__(self):
      print("constructor execution ")

t=test()     #Only one object is created , But execution is 4 times
t.__init__()
t.__init__()
t.__init__()



#Result:
# constructor execution
# constructor execution
# constructor execution
# constructor execution
