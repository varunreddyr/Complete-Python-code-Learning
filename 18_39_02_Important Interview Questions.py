# How to find the number of references to an object in Python?

import sys  # Importing the sys module to use the getrefcount() function

class Test:
    pass  # Creating an empty class named Test

# Creating an instance of the Test class
t1 = Test()

# Creating multiple references to the same object
t2 = t1  # t2 now points to the same object as t1
t3 = t2  # t3 also points to the same object
t4 = t3  # t4 also points to the same object

# Using sys.getrefcount() to check how many references exist for the object referenced by t1
print(sys.getrefcount(t1))  # Output: 5

# Explanation of Output:
# The reference count is 5 because:
# 1. t1 points to the object.
# 2. t2 also points to the same object.
# 3. t3 also points to the same object.
# 4. t4 also points to the same object.
# 5. The getrefcount() function itself creates a temporary reference while checking the count.

# Deleting some references
del t3, t4  # Removing two references to the object

# Checking reference count again
print(sys.getrefcount(t1))  # Output: 3

# Explanation of Output:
# The reference count is now 3 because:
# 1. t1 still references the object.
# 2. t2 still references the object.
# 3. The getrefcount() function temporarily adds a reference while executing.
