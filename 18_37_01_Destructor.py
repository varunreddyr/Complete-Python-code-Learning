# Destructor
import time
class Test:
    def __init__(self):
        print('Object Initialization Activities.....')

    def __del__(self):
        print('Fulfilling Last wish and performing object clean up activities...')

t=Test()
t=None
time.sleep(10)
print('End of application')



#Once the program gets end the application GC got executed .