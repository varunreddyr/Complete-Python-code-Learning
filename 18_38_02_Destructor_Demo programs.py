# Destructor
import time
class Test:
    def __init__(self):
        print('Object Initialization Activities.....')

    def __del__(self):
        print('Fulfilling Last wish and performing object clean up activities...')

l=[Test(),Test(),Test()]
del l
time.sleep(5)
print('End of application')

# Output:
# Object Initialization Activities.....
# Object Initialization Activities.....
# Object Initialization Activities.....
# Fulfilling Last wish and performing object clean up activities...
# Fulfilling Last wish and performing object clean up activities...
# Fulfilling Last wish and performing object clean up activities...
# End of application
