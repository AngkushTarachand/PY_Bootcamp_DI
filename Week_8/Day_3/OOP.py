class Animal:
    def __int__(self, animal_type, number_legs, sound):
        self.animal_type = animal_type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")


class Dog(Animal):
    def __int__(self, animal_type, number_legs, sound, is_lazy):
        super().__int__(type, number_legs, sound)
        self.is_lazy = is_lazy

    def fetch_ball(self):
        print("I am a dog, and i love fetching balls")

    def make_sound(self):
        super().make_sound()
        print("I am a DOGG !!! WOUAFF")


rex = Dog('dog', 4, "Wouaf")
print(rex.number_legs)
print(rex.sound)
rex.make_sound()
