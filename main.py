class Student:
    next_id = 100

    def __init__(self, name, department) -> None:
        self.student_id = self.next_id
        self.name = name
        self.department = department
        self.is_enrolled = False
        self.next_id += 1


class StudentDatabase:
    student_list = []

    def __init__(self) -> None:
        pass

    def add_student(self, name, department):
        student = Student(name, department)
        self.student_list.append(student)

    def enroll_student(self):
        print("Enter student id: ")
        id = int(input())

        for student in self.student_list:
            if student.student_id == id:
                if student.is_enrolled:
                    print(f"Student {id} already enrolled.")
                else:
                    student.is_enrolled = True
                    print(f"Student {id} enrollment has been done.")
                return

        print("Student id not found.")

    def drop_student(self):
        print("Enter student id: ")
        id = int(input())

        for student in self.student_list:
            if student.student_id == id:
                if student.is_enrolled:
                    student.is_enrolled = False
                    print(f"Student {id} has been dropped.")
                else:
                    print(f"Student {id} is not enrolled.")
                return

        print("Student id not found.")

    def view_student_info(self):
        for student in self.student_list:
            print(
                f"ID: {student.student_id}, Name: {student.name}, Department:"
                f" {student.department}, Enrolled: {student.is_enrolled}"
            )
