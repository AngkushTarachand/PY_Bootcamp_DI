class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        print('Person: {}, AgE: {} '.format(self.name, self.age))

    def __len__(self):
        return len(self.name)

    def __str__(self): # information for end users
        return f"name: {self.name}, age: {self.age}"

    def __repr__(self): # information for other developers
        return f"Person({self.name}, {self.age})"

    def __add__(self, other):
        return  Person1(self.name, other.age)

    def __mul__(self, other):
        return Person1(self.name, self.age*other.age)

person1 = Person("sarah", 25)
person2 = Person("Bob", 35)
person1()

print(len(person1))
print(str(person1))
print(repr(person1))

person3 = person1 + person2
print(person3.name)
print(person3.age)

