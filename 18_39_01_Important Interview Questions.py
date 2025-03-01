# Important Interview Questions:
# What is the difference between `del t` and `t = None`?
#
# 1. `del t`: Deletes the variable `t`, and if there are no other references to the object,
#             the garbage collector destroys the object, invoking the destructor (`__del__` method).
# 2. `t = None`: The variable `t` is assigned to `None`, breaking its reference to the object.
#               The destructor is triggered if no other references exist.
#               However, the variable `t` itself is not deleted and can be reassigned later.

import time  # Importing time module (not used in this script but can be helpful for testing delays)

class Test:
    def __init__(self):
        print('Object Initialization Activities.....')  # This message appears when an object is created.

    def __del__(self):
        print('Fulfilling last wish and performing object clean-up activities...')
        # This message appears when the object is destroyed.

# Creating an instance of the Test class, which triggers the constructor (__init__)
t = Test()

# Uncommenting `del t` will delete the reference variable `t` and, if no other references exist,
# Python's garbage collector will call the destructor (__del__).
# del t

print('End of application')  # Prints this message before script ends

# Assigning `t = None` removes the reference from `t` to the object.
# If no other references exist, the destructor (__del__) will be called.
# However, `t` itself is not deleted and can be reassigned.
# t = None




