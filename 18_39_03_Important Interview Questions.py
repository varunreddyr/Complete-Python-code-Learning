# How to find the number of references to an object in Python?
### **Difference Between Constructor and Destructor in Python**

# | Feature          | **Constructor (`__init__()`)**                      | **Destructor (`__del__()`)** |
# |-----------------|------------------------------------------------------|--------------------------------|
# | **Purpose**      | Initializes an object when it is created.           | Cleans up resources before an object is destroyed. |
# | **Method Name**  | `__init__(self)`  | `__del__(self)`                 |
# | **Called When**  | Automatically called when an object is created.     | Automatically called when an object is deleted or garbage collected. |
# | **Usage**        | Used to initialize attributes, allocate resources, or set up an object. | Used to release resources, close files, disconnect databases, etc. |
# | **Explicit Call Required?** | No, it is invoked automatically upon object creation. | No, it is invoked automatically when the object is no longer referenced. |
# | **Example Scenario** | Setting initial values for an object (e.g., opening a database connection). | Cleaning up resources before the object is destroyed (e.g., closing a file). |
#
# ---

### **Example Demonstrating Constructor and Destructor**

class Example:
    def __init__(self):
        print("Constructor: Object is created and initialized.")

    def __del__(self):
        print("Destructor: Object is being deleted and cleaned up.")

# Creating an object
obj = Example()  # Constructor is called automatically

# Deleting the object
del obj  # Destructor is called automatically


# ### **Key Takeaways**
# 1. **Constructor (`__init__()`)**:
#    - Initializes an object when it's created.
#    - Typically used to set up attributes or allocate resources.
#
# 2. **Destructor (`__del__()`)**:
#    - Cleans up an object before it is removed from memory.
#    - Useful for releasing external resources (e.g., closing files, database connections).
#
# Would you like a **real-world example** showing how a destructor is used to **release database connections**? 🚀