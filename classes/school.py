from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self,student_data):
        new_student = Student(**student_data)
        self.students.append(new_student)
        print(f"\nStudent:\n{new_student}\nwas sucessfully added to the School System.")
    
    def remove_student(self,removed_student_id):
        for x in range(len(self.students)):
            student = self.students[x]
            if removed_student_id == student.school_id:
                self.students.pop(x)
                print(f"\nStudent:\n{student}\nwas sucessfully removed from the School System.")
                break
    