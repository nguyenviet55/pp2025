class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0

    def set_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def calc_gpa(self):
        if len(self.marks) == 0:
            self.gpa = 0
        else:
            self.gpa = sum(self.marks.values()) / len(self.marks)
        return self.gpa
