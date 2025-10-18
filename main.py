class StudentDatabase:
    __student_list = []

    @classmethod
    def add_student(cls, student):
        cls.__student_list.append(student)

    def enroll_student(self):
        print("Enter student id: ")
        id = int(input())

        for student in self.__student_list:
            if student.id == id:
                if student.enroll:
                    print(f"Student {id} already enrolled.")
                else:
                    student.enroll = True
                    print(f"Student {id} enrollment has been done.")
                return

        print("Student id not found.")

    def drop_student(self):
        print("Enter student id: ")
        id = int(input())

        for student in self.__student_list:
            if student.id == id:
                if student.enroll:
                    student.enroll = False
                    print(f"Student {id} has been dropped.")
                else:
                    print(f"Student {id} is not enrolled.")
                return

        print("Student id not found.")

    @classmethod
    def view_student_info(cls):
        for student in cls.__student_list:
            print(
                f"ID: {student.id}, Name: {student.name}, "
                f"Department: {student.department}, "
                f"Enrolled: {student.enroll}"
            )

    @classmethod
    def total_student(cls):
        print(f"Total Students: {len(cls.__student_list)}")


class Student:
    __next_id = 100

    def __init__(self, name, department) -> None:
        self.__student_id = Student.__next_id
        self._name = name
        self._department = department
        self.__is_enrolled = False
        Student.__next_id += 1

        StudentDatabase.add_student(self)

    @property
    def id(self):
        return self.__student_id

    @property
    def name(self):
        return self._name

    @property
    def department(self):
        return self._department

    @property
    def enroll(self):
        return self.__is_enrolled

    @enroll.setter
    def enroll(self, value):
        self.__is_enrolled = value


Student("Arnab Saha", "Computer Science")
Student("Rafi Khan", "Electrical Engineering")
Student("Nusrat Jahan", "Business Administration")
Student("Tanvir Ahmed", "Mechanical Engineering")
Student("Mehedi Hasan", "Civil Engineering")
Student("Farhana Rahman", "Computer Science")
Student("Sumaiya Akter", "Pharmacy")
Student("Mahmudul Islam", "Economics")
Student("Shakil Chowdhury", "Law")
Student("Tania Noor", "Architecture")

db = StudentDatabase()


while True:
    print("---------------Student Database---------------")
    print(
        """1. View All Students
2. Enroll Student
3. Drop Student
4. Total Students
5. Exit
Enter you option (1-5):"""
    )
    x = int(input())
    if x == 1:
        db.view_student_info()
    elif x == 2:
        db.enroll_student()
    elif x == 3:
        db.drop_student()
    elif x == 4:
        db.total_student()
    elif x == 5:
        break
    else:
        print("Invalid option.")
