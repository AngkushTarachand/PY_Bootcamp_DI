class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = age

    def bark(self):
        return "{} is barking".format(self.name)

    def run_speed(self):
        return "the dog is running".format(self.weight/self.age*10)

    def fight(self, other_dog):
        dog_criteria = (self.weight**2)/self.age*10
        other_dog_criteria = (other_dog.weight**2)/other_dog.age*10

        if dog_criteria > other_dog_criteria:
            return self.name
        else:
            return other_dog.name


Ben = Dog("Ben", 4, 14)
Cliford = Dog("Cliford", 5, 30)
Bill = Dog("Bill", 9, 23)
other_dog = Bill

print(Ben.fight(Bill))
print(Ben.bark())
