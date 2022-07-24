class Dog:
    def __int__(self, name, age, weight):
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

Ben = Dog("Ben")
Cliford = Dog("Cliford")
Bill = Dog("Bill")
