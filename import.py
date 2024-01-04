import re
import sys
grades = {90: 'A', 80: 'B', 70: 'C', 60: 'D', 50: 'E', 0: 'FAIL'}
class Student:
    def set_name(self, name):
        self.name = name

    def set_marks(self, mark_lst):
        self.mark_lst = mark_lst

    def set_lowest_mark(self, lowest_mark):
        self.lowest_mark = lowest_mark

    def set_highest_mark(self, highest_mark):
        self.highest_mark = highest_mark

    def set_average_mark(self, average_mark):
        self.average_mark = average_mark

    def validate_mark(self):
        if self.lowest_mark > 100 or self.highest_mark > 100:
            print("ERROR: Marks should be in the range 0-100")
            return -1
        else:
            return 0

    def validate_name(self):
        if re.fullmatch('[A-Za-z]{2,25}([A-Za-z]{1,25})?', self.name):
            return 0
        else:
            print("ERROR: Invalid name provided")
            return -1

    def validate_subject_count(self):
        if len(self.mark_lst) < 5:
            print("ERROR: At least 5 subject marks are required")
            return -1
        elif len(self.mark_lst) > 15:
            print("ERROR: More than 15 subject marks are not allowed")
            return -1
        else:
            return 0

    def show(self):
        print("Name:", self.name)
        print("Average", self.average_mark)
        print("Highest Grade:", self.compute_grade(self.highest_mark))
        print("Lowest Grade:", self.compute_grade(self.lowest_mark))

    @staticmethod
    def compute_grade(mark):
        for min_score, grade in grades.items():
            if mark >= min_score:
                return grade


def new_student_data():
    student = Student()
    student.set_name(input("Enter the name of the student: "))
    if student.validate_name() == -1:
        return
    print("Enter the marks for subject with comma separation")
    marks = list(map(int, input().split(',')))
    student.set_marks(marks)
    if student.validate_subject_count() == -1:
        return
    student.set_average_mark(sum(marks) / len(marks))
    student.set_lowest_mark(min(marks))
    student.set_highest_mark(max(marks))
    if student.validate_mark() == -1:
        return
    student.show()


if __name__ == '__main__':
    print("Enter '1' to add new student details")
    print("Enter '2' to exit the program")
    while 1:
        option = int(input("Enter the option: "))
        if option == 1:
            new_student_data()
        elif option == 2:
            sys.exit()
        else:
            print("Invalid option")
