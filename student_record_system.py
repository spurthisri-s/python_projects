class Student:

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)


name = input("Enter Name: ")
rollno = input("Enter Roll Number: ")
marks = input("Enter Marks: ")

student = Student(name, rollno, marks)

student.display()