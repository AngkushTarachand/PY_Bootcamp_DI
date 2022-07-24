import random

class Dog():
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


class PetDog(Dog):
    def __int__(self, trained):
        self.trained = trained

        trained = False

    def train(self):
        print("bark")
        trained = True

    def play(self, *args):
        print("{} all play together".format{*args})

    def do_a_trick:
        do_a_trick_dict = {
            1: [f'{self.name} does a barrel roll'],
            2: [f'{self.name} stands on his back legs'],
            3: [f'{self.name} shakes your head'],
            4: [f'{self.name} plays dead']
        }

