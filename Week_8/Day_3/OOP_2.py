class Teacher:

    def set_grade(self, student, grade):
        student.grade = grade


class Student:
    def __int__(self, name):
        self.__grade = 0
        self.name = name


bob = Student("bob")
alice = Student("alice")

teacher = Teacher()
teacher.set_grade(bob, 95)
teacher.set_grade(alice, 92)

print(bob.grade)
print(alice.grade)

class Parrot():

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin():

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
# >> Parrot can fly

flying_test(peggy)
# >> Penguin can't fly
