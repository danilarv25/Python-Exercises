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
    def __init__(self, teacher, topic, date):
        self.teacher = teacher
        self.topic = topic
        self.date = date
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

    def show_teacher(self):
        print(f"This lecture's teacher: {self.teacher.name}")
        return

class Teacher:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def greet(self):
        print("Hello class!\n")
        return

teacher1 = Teacher("John Smith", "Mathematics")
session = Lecture(teacher1, "Math 101", "24-10-2025")
session.show_teacher()
teacher1.greet()

student1 = Student("Bob", "B", 19)
student2 = Student("Jill", "B", 21)
student3 = Student("Bartholomew", "B", 22)

session.log_student(student1)
session.log_student(student2)
session.log_student(student3)

session.show_attendence()

session.student_logout(student3)

session.show_attendence()