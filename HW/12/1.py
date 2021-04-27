"""
 Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде уникального набора
 объектов
 `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
`grades` и тп), а так же необходимый набор методов экземпляра для работы с этими объектами.
    Реализовать функционал, который позволит:
     1. Покинуть студенту группу
     2. Перевестись в другую группу
     3. Покзать средний балл отдельного студента
     4. Показать средний балл по группе
     (по желанию и возможностям можно еще добавить функционала)
"""
#from statistics import mean
import uuid

class Student:
    def __init__(self, name, age, grades, group):
        self.name = name is str
        self.age = age is int
        self.grades = grades is {}
        self.group = group
        self._id = uuid.uuid4()

    def leave_group(self):
        self.group.delete_student(self)

    def change_group(self, another_group):
        self.group.delete_student(self)
        another_group.add_student(self)

    def become_senior(self, senior):
        senior.upgrade(self)

    @property
    def average_grades(self):
        return sum(self.grades.values()) / len(self.grades)

class Group:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def delete_student(self, student: Student):
        self.students.pop(student._id, None)
        student.group = None

    def add_student(self, student):
        self.students.setdefault(student._id, student)
        student.group = self

#можно ли так?
#    @property
#    def average_grades_g(self):
#        return mean([student.average_grades for student in self.students.values()])


    @property
    def average_grades(self):
        return sum([student.average_grades for student in self.students.values()]) / len(self.students)

class Seniors:
    def __init__(self):
        self.students = {}

    def upgrade(self, student):
        self.students.setdefault(student)

def check():
    group1 = Group(name='A')
    group2 = Group(name='B')
    qw = Student(name="QW", age=15, grades={'math': 10, 'physic': 5}, group=group1)
    zx = Student(name="ZX", age=16, grades={'math': 5, 'physic': 7}, group=group2)
    senior = Seniors()
    print(qw.name)
    group1.add_student(zx)
    senior.upgrade(zx)