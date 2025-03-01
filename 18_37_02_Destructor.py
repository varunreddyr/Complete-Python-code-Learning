# Destructor

class Test:
    def __init__(self):
        print('Object Initialization Activities.....')

    def __del__(self):
        print('Fulfilling Last wish and performing object clean up activities...')

t1=Test()
t2=Test()

print('End of application')



# Output:
# Object Initialization Activities.....
# Object Initialization Activities.....
# End of application
# Fulfilling Last wish and performing object clean up activities...
# Fulfilling Last wish and performing object clean up activities...
