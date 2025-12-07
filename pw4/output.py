def list_students(students):
    print("\n==== Student List ====")
    for s in students:
        print(f"{s.sid} - {s.name} - DOB: {s.dob}")

def list_courses(courses):
    print("\n==== Course List ====")
    for c in courses:
        print(f"{c.cid} - {c.name} ({c.credit} credits)")

def show_marks(students, course_id):
    print(f"\n==== Marks of Course {course_id} ====")
    for s in students:
        if course_id in s.marks:
            print(f"{s.name}: {s.marks[course_id]}")
        else:
            print(f"{s.name}: No mark!")

def show_gpa(students):
    print("\n==== GPA Ranking ====")
    students.sort(key=lambda x: x.calc_gpa(), reverse=True)
    for s in students:
        print(f"{s.name}: GPA = {s.gpa:.2f}")
