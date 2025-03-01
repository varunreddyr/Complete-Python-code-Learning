# 5. Hybrid Inheritance:
# Hybrid Inheritance is a combination of two or more types of inheritance in a single program.
# It helps in reusing code from multiple parent classes while maintaining a structured relationship.
# Since multiple inheritance is involved, Python follows Method Resolution Order (MRO)
# to resolve method conflicts.

# Key Points:
# ✔ Hybrid Inheritance combines different types of inheritance (Single, Multiple, Hierarchical).
# ✔ Method Resolution Order (MRO) ensures correct method execution.
# ✔ Useful for designing complex class relationships while ensuring code reusability.
# ✔ Be careful with method conflicts and diamond problems when using multiple inheritance.


# Base class (Superclass)
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Intermediate class inheriting from Animal (Single Inheritance)
class Mammal(Animal):
    def has_hair(self):
        print("Mammals have hair")

# Another class inheriting from Animal (Hierarchical Inheritance)
class Bird(Animal):
    def can_fly(self):
        print("Birds can fly")

# Child class inheriting from Mammal and Bird (Multiple Inheritance)
class Bat(Mammal, Bird):
    def is_bat(self):
        print("Bat is a mammal but can fly like a bird")

# Creating object of Bat class
bat = Bat()

# Calling methods from different parent classes
bat.speak()     # Inherited from Animal
bat.has_hair()  # Inherited from Mammal
bat.can_fly()   # Inherited from Bird
bat.is_bat()    # Defined in Bat class
