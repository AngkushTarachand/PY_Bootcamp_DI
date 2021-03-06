class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk)


class Cat:
    id_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def __int__(self, name="Siamese", age=5):
        super().__init__(name, age)


all_cats = [Bengal, Chartreux, Siamese]

for cat in all_cats:
    sara_pet = Cat(cat,89 )
    sara_pet.walk()


