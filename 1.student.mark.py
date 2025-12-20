students = []
courses = []
marks = {}

def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        sid = input("Student ID: ")
        for s in students:
            if s["id"] == sid:
                print("Student ID already exists!")
                return

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
    cid = input("Enter course ID: ")
    found = False
    for c in courses:
        if c["id"] == cid:
            found = True

    if not found:
        print("Course not found!")
        return

    marks[cid] = {}
    for s in students:
        score = float(input(f"Enter mark for {s['name']}: "))
        if score < 0 or score > 10:
            print("Invalid mark!")
            return

        marks[cid][s["id"]] = score

def list_students():
    for s in students:
        print(s)

def list_courses():
    for c in courses:
        print(c)

def show_marks():
    cid = input("Enter course ID: ")

    # dùng lại IF 2
    if cid not in marks:
        print("No marks for this course!")
        return

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

    if choice == 1:
        input_students()
    elif choice == 2:
        input_courses()
    elif choice == 3:
        input_marks()
    elif choice == 4:
        list_students()
    elif choice == 5:
        list_courses()
    elif choice == 6:
        show_marks()
    elif choice == 0:
        break
    else:
        print("Invalid choice!")
