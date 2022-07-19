class School:
    name = "School A"
    num_of_students = 200
    num_of_classes = 10


# class Car:
#     pass


# car1 = Car()
# car1.color = "Red"
# car1.type = "Ford"
# car1.brand = "Mustang"
#
# car2 = Car()
# car2.color = "Blue"
# car2.type = "Toyota"
# car2.brand = "Prius"

# print(car1.color)


class Car:
    def __int__(self, color, type1, brand):
        print("at the init")
        self.color = color
        self.type = type1
        self.brand = brand

    def turn_right(self):
        print(f"Turning right the car of type {self.type}")

    def speed(self):
        print("speeding")

    def slow(self):
        print("slowing down")

    def turn_left(self):
        print("turning left")


car1 = ("Red", "Ford", "Mustang")
car2 = ("Blue", "Toyota", "Prius")

# car1.turn_right()
Car.turn_right(car1)


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)


first_person = Person("John", 36)
first_person.show_details()
