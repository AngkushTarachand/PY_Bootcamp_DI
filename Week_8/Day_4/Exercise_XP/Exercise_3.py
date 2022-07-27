class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

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
        self.trained = False

    def train(self):
        print(f"{self.name}bark")
        self.trained = True

    def play(self, *args):
        print(f"{self.name} all play together")

    def do_a_trick(self):
        do_a_trick_dict = {
            1: [f'{self.name} does a barrel roll'],
            2: [f'{self.name} stands on his back legs'],
            3: [f'{self.name} shakes your head'],
            4: [f'{self.name} plays dead']
        }
        return do_a_trick_dict


Ben = Dog(12, 16, 23)
print(PetDog(Dog(12, 16, 23)))
