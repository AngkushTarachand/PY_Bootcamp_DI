# # class attribute
#
# class Dog:
#
#     counter = 0
#
#     def __init__(self, name):
#         self.name = name
#
#         Dog.counter += 1
#
#
# rex = Dog("Rex")
# lacy = Dog("Lucy")
#
# print(rex.name)
# print(lacy.name)
#
# print(rex.counter)
# print(lacy.counter)
# print(Dog.counter)  # This is the best practice to access class attribute.
#
#
# class Circle:
#     color = "red"
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#
#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor
#
#     @staticmethod # => decoration is added to static method
#     def get_color():  # => no need of self, since it is universal, hence decoration used
#         return Circle.color
#     # def get_color(self): => it is static
#
#
# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)
#
# class Vehicle:
#     def __init__(self, wheels_number):
#         self.__wheels_number = wheels_number
#
#     @classmethod
#     def create_car(cls):
#         return cls(4)  # vehicle(4)
#
#     # getter
#     @property
#     def wheels_number(self):
#         return self.__wheels_number
#
#     @wheels_number.setter
#     def wheels_number(self, new_wheels_number):
#         if new_wheels_number < 1:
#             print("invalid wheel number")
#         else:
#             self.__wheels_number = new_wheels_number
#
#
# toyota = Vehicle.create_car()
# mazda = Vehicle.create_car()
#
# toyota.__wheels_number = 2
# # print(toyota.__wheels_number)
# # print(mazda.__wheels_number)
#
# toyota.__wheels_number = 5
# mazda.__wheels_number = -1
#
# class Person:
#     used_names = set()
#
#     def __init__(self, name, age):
#         if name in Person.used_names:
#             name = input("THat name is taken.")
#
#     @classmethod
#     def fromYear(cls, name, birth_year):
#         THIS_YEAR = 2022
#         return cls(name, THIS_YEAR - birth_year)

    # @property
