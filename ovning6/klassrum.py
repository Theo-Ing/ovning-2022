# Studenter med ögonfärg, höjd, namn och ålder

class Student:
    def __init__(self, age, height, eye):
        self.age = age
        self.height = height
        self.eye_color = eye

class ClassRoom:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, height, eye):
        self.students[name] = Student(age, height, eye)

    def move_student(self, name, new_class):
        new_class.students[name] = self.students[name]
        del self.students[name]


klass_A = ClassRoom()
klass_A.add_student("erik", 12, 140, "grön")
print(klass_A.students)
klass_B = ClassRoom()
klass_A.move_student("erik", klass_B)
print(klass_A.students)
print(klass_B.students)