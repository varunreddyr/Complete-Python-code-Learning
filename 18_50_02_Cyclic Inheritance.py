# 6.Cyclic Inheritance:
# 🔹 Cyclic Inheritance occurs when a class inherits from itself either directly
#    or indirectly, creating an infinite loop in the inheritance chain.
# 🔹 Python does not allow cyclic inheritance, and it will result in an error.

# Why Cyclic Inheritance is Not Allowed?
# Infinite Recursion: The interpreter doesn’t know where to stop while resolving method resolution order (MRO).
# Confusing Class Hierarchy: It violates OOP principles, making code unreadable and unmaintainable.
# Breaks Python’s MRO Algorithm: Python resolves method calls linearly, and cyclic inheritance prevents proper resolution.
# 🔹 How to Avoid Cyclic Inheritance?
# ✔ Ensure a clear parent-child relationship without circular dependencies.
# ✔ Use composition (HAS-A relationship) instead of forcing unnecessary inheritance.
# ✔ Keep inheritance hierarchy simple and logical.












