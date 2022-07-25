class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name
        self.animals_dict = {}

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print("Already in list")
        else:
            self.animals.append(new_animal.capitalize())

    def get_animal(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print("Not in list")

    def sort_animals(self):
        # sort list
        self.animals.sort()
        print(self.animals)
        counter = 1
        for species in self.animals:
            index = self.animals.index(species)
            if self.animals[index][0] == self.animals[index-1][0]:
                if (counter - 1) in self.animals_dict:
                    self.animals_dict[counter-1].append(species)
            else:
                self.animals_dict[counter] = [species]
                counter += 1
        print(self.animals_dict)

    def get_group(self):
        for each in self.animals_dict.values():
            print(each)


z = Zoo("Casela")
z.add_animal("Ape")
z.add_animal("Baboon")
z.add_animal("Bear")
z.add_animal("Cat")
z.add_animal("Cougar")
z.add_animal("Emu")
z.add_animal("Eel")
z.get_animal()
z.sell_animal("Ape")
z.sell_animal("elephant")
z.sort_animals()
z.get_group()

y = Zoo("ramat_gan_safari")
animal_to_be_added = input("Which animal should be added --> ").capitalize()
y.add_animal(animal_to_be_added)
y.sort_animals()
