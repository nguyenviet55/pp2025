import math
import numpy as np

# =========================
#        OOP CLASSES
# =========================
class Student:
    def __init__(self, sid, name, dob):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
        self.gpa = 0  

    def get_id(self): return self.__sid
    def get_name(self): return self.__name

    def calculate_gpa(self, marks):
        weighted = 0
        total_credits = 0
        for m in marks:
            if m.sid == self.__sid:
                weighted += m.mark * m.course_credits
                total_credits += m.course_credits
        if total_credits == 0: 
            self.gpa = 0
        else:
            self.gpa = round(weighted / total_credits, 2)

    def display(self):
        print(f"[{self.__sid}] {self.__name} | DOB: {self.__dob} | GPA: {self.gpa}")

class Course:
    def __init__(self, cid, name, credits):
        self.__cid = cid
        self.__name = name
        self.__credits = credits

    def get_id(self): return self.__cid
    def get_name(self): return self.__name
    def get_credits(self): return self.__credits

    def display(self):
        print(f"[{self.__cid}] {self.__name} ({self.__credits} credits)")

class Mark:
    def __init__(self, sid, cid, mark, credits):
        self.sid = sid
        self.cid = cid
        self.mark = mark
        self.course_credits = credits

    def display(self):
        print(f"{self.sid} {self.cid}: {self.mark}")

# =========================
#        DATA STORAGE
# =========================
students = []
courses = []
marks = []

# =========================
#        FUNCTIONS
# =========================
def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("Date of birth: ")
        students.append(Student(sid, name, dob))
    print(">> Students added.\n")

def list_students():
    print("\n=== STUDENTS LIST ===")
    for s in students: s.display()

def input_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        cid = input("Course ID: ")
        name = input("Course name: ")
        credits = int(input("Credits: "))
        courses.append(Course(cid, name, credits))
    print(">> Courses added.\n")

def list_courses():
    print("\n=== COURSES LIST ===")
    for c in courses: c.display()

def input_marks():
    cid = input("Enter course ID to input marks: ")
    course = next((c for c in courses if c.get_id() == cid), None)
    if not course:
        print("!! Course not found!")
        return
    
    for s in students:
        raw = float(input(f"Mark for {s.get_name()}: "))
        fixed = math.floor(raw * 10) / 10  # floor 1 decimal
        marks.append(Mark(s.get_id(), cid, fixed, course.get_credits()))
    print(">> Marks added.\n")

def list_marks():
    print("\n=== MARKS LIST ===")
    for m in marks: m.display()

def sort_gpa():
    for s in students: s.calculate_gpa(marks)
    students.sort(key=lambda x: x.gpa, reverse=True)
    print("\n=== SORTED BY GPA DESCENDING ===")
    list_students()

# =========================
#            MENU
# =========================
def menu():
    while True:
        print("""
========== STUDENT MANAGEMENT ==========
1. Input students
2. List students
3. Input courses
4. List courses
5. Input marks
6. List marks
7. Sort students by GPA
0. Exit
========================================""")
        choice = input("Choose an option: ")

        if choice == "1": input_students()
        elif choice == "2": list_students()
        elif choice == "3": input_courses()
        elif choice == "4": list_courses()
        elif choice == "5": input_marks()
        elif choice == "6": list_marks()
        elif choice == "7": sort_gpa()
        elif choice == "0":
            print("Bye! See you.")
            break
        else:
            print("Invalid choice!")

menu()
