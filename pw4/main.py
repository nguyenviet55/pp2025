from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_marks, show_gpa

def main():
    students = []
    courses = []

    while True:
        print("\n=========== MENU ===========")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks of a course")
        print("7. Sort students by GPA")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            students = input_students()
        elif choice == "2":
            courses = input_courses()
        elif choice == "3":
            input_marks(students, courses)
        elif choice == "4":
            list_students(students)
        elif choice == "5":
            list_courses(courses)
        elif choice == "6":
            cid = input("Course ID: ")
            show_marks(students, cid)
        elif choice == "7":
            show_gpa(students)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
