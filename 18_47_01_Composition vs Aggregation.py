# Composition vs Aggregation:
# Both Composition and Aggregation represent the HAS-A relationship in Object-Oriented Programming (OOP).
# Composition: Strong relationship (the contained object cannot exist without the container).
# Aggregation: Weak relationship (the contained object can exist independently).

# Composition:
# ✔ One class owns another class, and the owned object cannot exist independently.
# ✔ When the container (parent) object is destroyed, the contained (child) object is also destroyed.
# ✔ Used when one object is entirely dependent on another.e contained object can exist independently).

# class University:
#     def __init__(self):
#         self.dept=self.Department()
#     class Department:
#         pass
# u=University()

# Aggregation:
# ✔ The contained object is passed from outside, meaning it can exist independently.
# ✔ Even if the parent object is deleted, the child object still exists.
# ✔ Used when objects have an association but don’t depend on each other.

# class Professor:
#     pass
# class Department:
#     def __init__(self,professor):
#         self.professor=professor
#
# professor=Professor()
# csdept=Department(Professor)
# itdept=Department(Professor)

