import math
import random

def add_student(students, name, subjects):
    students[name] = subjects
    return

def update_grade(students, name, subject, new_score):
    if new_score > students[name][subject]:
        students[name][subject] = new_score
    else:
        print(f"{name}'s new score ({new_score}) is lower. Keeping the older, higher score of {students[name][subject]}.\n")
    return

def add_subject(students, name, subject, score):
    students[name].update({subject : score})
    return

def print_student(students, name = None):
    if name == None:
        for i in students:
            print(i)
            for j in students[i]:
                print("   ",j,":", students[i][j])
        print("")
    else:
        print(name)
        for i in students[name]:
            print("   ",i,":", students[name][i])
        print("")
    return

def get_average(students, name):
    avg = 0
    subjects = 0
    for i in students[name]:
        avg += students[name][i]
        subjects += 1
    avg = avg/subjects
    return round(avg,2)

students = {
    "Alice" : {"Math" : 87, "English" : 83},
    "John" : {"Math" : 79, "English" : 90}
}

print_student(students)
update_grade(students,"Alice","Math",90)
update_grade(students,"John","Math",75)
print(students,"\n")
add_student(students, "Steve", {"History" : 95, "Biology" : 73})
print(students,"\n")
add_subject(students,"Alice","History",77)
print(students,"\n")
print_student(students, "John")
print(f"Alice's average grade is: {get_average(students, "Alice")}")






# print("Showing Alice's math score")
# print(students["Alice"]["Math"])
#
# print("Showing John's english score")
# print(students["John"]["English"])
#
# print("Adding 'History' subject and score")
# students["Alice"].update({"History" : 95})
# print(students["Alice"])
#
# print("Changing John's math score to 82")
# print(f"Old score: {students["John"]["Math"]}")
# students["John"]["Math"] = 82
# print(f"New score: {students["John"]["Math"]}")
#
#
#
# students["Steve"] = {"Math" : 98, "English" : 71} # or students.update({"Steve" : {"Math" : 98, "English" : 71}})
# del students["Alice"]["Math"] # or students["Alice"].pop("Math")