# Destructor
import time
class Test:
    def __init__(self):
        print('Object Initialization Activities.....')

    def __del__(self):
        print('Fulfilling Last wish and performing object clean up activities...')

t1=Test()
t2=t1
t3=t1
del t1
time.sleep(5)
print('Object not destroyed after deleting t1')
del t2
time.sleep(5)
print('Object not destroyed even after deleting t2')
print('Removing last reference')
del t3
print('End of application...')


