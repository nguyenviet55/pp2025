students = []
courses = []
marks = {}

def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")
        students.append({"id": sid, "name": name, "dob": dob})

def input_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        cid = input("Course ID: ")
        cname = input("Course name: ")
        courses.append({"id": cid, "name": cname})

def input_marks():
    cid = input("Enter course ID to input marks: ")
    marks[cid] = {}
    for s in students:
        score = float(input(f"Enter mark for {s['name']}: "))
        marks[cid][s["id"]] = score

def list_students():
    for s in students:
        print(s)

def list_courses():
    for c in courses:
        print(c)

def show_marks():
    cid = input("Enter course ID: ")
    print(marks[cid])

while True:
    print("\n--- Student Mark Management ---")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show marks")
    print("0. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1: input_students()
    elif choice == 2: input_courses()
    elif choice == 3: input_marks()
    elif choice == 4: list_students()
    elif choice == 5: list_courses()
    elif choice == 6: show_marks()
    elif choice == 0: break
    else:
        print("Invalid choice!")
