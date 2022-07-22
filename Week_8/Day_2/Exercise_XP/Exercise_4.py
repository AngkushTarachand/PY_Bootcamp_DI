class Zoo:
    def __int__(self, zoo_name):
        self.animals = []
        self.zoo_name = name

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print("Already in list")
        else:
            self.animals.append(new_animal)

    def get_animal(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print("Not in list")

    def sort_animals(self):
        # Initialise dictionary
        animals_dict = {}

        # sort list
        self.animals.sort()
        counter = 1
        # looping for first character and group
        animal_list_dict = []
        for animal in self.animals:
            index = self.animals.index(animal)
            if self.animals[index][0] is self.animals[index-1][0]:
                animals_dict[counter] = animal_list_dict.append(animal)
            else:
                counter = counter + 1
                animals_dict[counter] = animal



