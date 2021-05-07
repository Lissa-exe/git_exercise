class Figures:

    def perimeter(self):
        raise NotImplementedError

    def square(self):
        raise NotImplementedError

class Triangle(Figures):
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def validation_of_triangle(self, side_1, side_2, side_3):
        if side_1 > (side_2 + side_3):
            raise ValueError('1Incorrect format! Side is need to be mere than sum of other two sides.')
        if side_2 > (side_1 + side_3):
            raise ValueError('2Incorrect format! Side is need to be mere than sum of other two sides.')
        if side_3 > (side_1 + side_2):
            raise ValueError('3Incorrect format! Side is need to be mere than sum of other two sides.')

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def square(self):
        p = self.perimeter() / 2
        return (p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)) ** 0.5

class Foursquare(Figures):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def square(self):
        return self.side * self.side

class Rectangle(Figures):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def perimeter(self):
        return 2 * (self.side_1 + self.side_2)

    def square(self):
        return self.side_1 * self.side_2

############

"""
Реализовать класс Person, у которого должно быть два атрибута: age и name. 
Также у него должен быть следующий набор методов:
    1.def know(self, another_person_object)
    который позволяет добавить другого человека в список знакомых (лист __friends (обязательно приватный атрибут)).
    2.def is_known(self, another_person_object)
    который возвращает знакомы ли два человека (True/False)
"""

class Person:
    def __init__(self, age, name, _id):
        self.age = age
        self.name = name
        self.__friends = {}
        self.id = _id


    def know(self, another_person_object):
        self.__friends.setdefault(another_person_object.id, another_person_object)

    def is_known(self, another_person_object):
        return another_person_object in list(self.__friends)

person_1 = Person(10, 'A', 1)
person_2 = Person(7, 'B', 2)

print(person_1.is_known(person_2))

person_1.know(person_2)

print(person_1.is_known(person_2))
