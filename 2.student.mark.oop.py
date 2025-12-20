class Student:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__dob = None

    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student name: ")
        self.__dob = input("Date of birth: ")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__id} - {self.__name} - {self.__dob}"


class Course:
    def __init__(self):
        self.__id = None
        self.__name = None

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course name: ")

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"{self.__id} - {self.__name}"


class Mark:
    def __init__(self, course):
        self.course = course
        self.marks = {}

    def input(self, student):
        score = float(input(f"Enter mark for {student.get_name()}: "))

        # IF 3: kiểm tra điểm hợp lệ
        if score < 0 or score > 10:
            print("Invalid mark (0–10)!")
            return

        self.marks[student.get_id()] = score

    def show(self):
        print(f"Marks for course {self.course.get_id()}:")
        for sid, score in self.marks.items():
            print(f"{sid}: {score}")


class Manager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        n = int(input("Enter number of students: "))
        for _ in range(n):
            s = Student()
            s.input()

            # IF 1: kiểm tra trùng Student ID
            for st in self.students:
                if st.get_id() == s.get_id():
                    print("Student ID already exists!")
                    return

            self.students.append(s)

    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for _ in range(n):
            c = Course()
            c.input()
            self.courses.append(c)

    def input_marks(self):
        cid = input("Enter course ID to input marks: ")

        # IF 2: kiểm tra course tồn tại
        course = next((c for c in self.courses if c.get_id() == cid), None)
        if not course:
            print("Course not found!")
            return

        self.marks[cid] = Mark(course)
        for student in self.students:
            self.marks[cid].input(student)

    def list_students(self):
        for s in self.students:
            print(s)

    def list_courses(self):
        for c in self.courses:
            print(c)

    def show_marks(self):
        cid = input("Enter course ID: ")

        # dùng lại IF 2
        if cid not in self.marks:
            print("No marks for this course!")
            return

        self.marks[cid].show()


# ===== MAIN =====
m = Manager()

while True:
    print("\n--- Student Mark Management OOP ---")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show marks")
    print("0. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1: m.input_students()
    elif choice == 2: m.input_courses()
    elif choice == 3: m.input_marks()
    elif choice == 4: m.list_students()
    elif choice == 5: m.list_courses()
    elif choice == 6: m.show_marks()
    elif choice == 0: break
    else:
        print("Invalid choice!")
