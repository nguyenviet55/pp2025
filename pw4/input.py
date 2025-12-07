from domains.student import Student
from domains.course import Course

def input_students():
    students = []
    n = int(input("Number of students: "))
    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of birth: ")
        students.append(Student(sid, name, dob))
    return students

def input_courses():
    courses = []
    m = int(input("Number of courses: "))
    for _ in range(m):
        cid = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Course credits: "))
        courses.append(Course(cid, name, credit))
    return courses

def input_marks(students, courses):
    course_id = input("Enter course ID to input marks: ")
    found = [c for c in courses if c.cid == course_id]

    if not found:
        print("Course not found!")
        return

    for s in students:
        try:
            mark = float(input(f"Mark for {s.name}: "))
            s.set_mark(course_id, mark)
        except:
            print("Invalid! Try again.")
