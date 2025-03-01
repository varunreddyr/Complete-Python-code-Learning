class Student:
    def __init__(self, name, rollno, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def talk(self) -> None:
        print("Hello I am :", self.name)
        print("My roll no", self.rollno)
        print("My marks are ", self.marks)


s1 = Student("Varun", 20137441, 100)
s1.talk()