class Student:
    """Note:You can use delf instead of self keyword"""
    def __init__(delf, name, rollno, marks):
       delf.rollno = rollno
       delf.name = name
       delf.marks = marks

    def talk(kelf) -> None:       # You can use Kelf instead of self , It always refers to current object That's it
        print("Hello I am :", kelf.name)
        print("My roll no", kelf.rollno)
        print("My marks are ",kelf.marks)


s1 = Student("Varun", 100, 20137441)
s2 = Student("Arun", 100, 20137442)
s1.talk()
s2.talk()