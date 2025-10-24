import random

class Student:
    def __init__(self, name, group, age):
        self.name = name
        self.group = group
        self.age = age

    def greet(self, times):
        for i in range(times):
            type = random.randint(1,3)
            if type == 1:
                print("Hello.")
            elif type == 2:
                print("Wassup!")
            else:
                print("Yoooooooooooo!")

        return

class Lecture:
    def __init__(self):
        self.attendence = []

    def log_student(self, student):
        student.greet(1)
        self.attendence.append(student)
        print(f"{student.name} has been logged\n")
        return

    def student_logout(self, student):
        self.attendence.remove(student)
        print(f"{student.name} has been removed")
        return

    def show_attendence(self):
        print("\nPresent Students:\n")
        for i in self.attendence:
            print(i.name)
        print("")

session = Lecture()

student1 = Student("Bob", "B", 19)
student2 = Student("Jill", "B", 21)
student3 = Student("Bartholomew", "B", 22)

session.log_student(student1)
session.log_student(student2)
session.log_student(student3)

session.show_attendence()

session.student_logout(student3)

session.show_attendence()