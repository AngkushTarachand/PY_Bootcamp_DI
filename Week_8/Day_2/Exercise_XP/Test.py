import collections


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print("Already in list")
        else:
            self.animals.append(new_animal)

    def get_animal(self):
        pass
        # for animal in self.animals:
        #     print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            pass
            # print("Not in list")

    def sort_animals(self):
        # Initialise dictionary
        animals_dict = {}

        # sort list
        self.animals.sort()
        print(self.animals)
        counter = 1
        # looping for first character and group
        # animal_list_dict = []
        for animal in self.animals:
            # print(animal)
            index = self.animals.index(animal)
            # print(index, animal, self.animals[index], self.animals[index-1])
            # if self.animals[index][0] == self.animals[index-1][0]:
            #     print(animal)
            #     # animals_dict[1].append(animal)
            #
            # else:
            #     animals_dict[counter].append(animal)
            #     counter += 1
            #     print(animals_dict)


z = Zoo("Casela")
z.add_animal("Ape")
z.add_animal("Baboon")
z.add_animal("Bear")
z.add_animal("Cat")
z.add_animal("Emu")
z.get_animal()
z.sell_animal("Ape")
z.sell_animal("elephant")
z.sort_animals()

zoo_dict = collections.defaultdict(list)
zoo_dict1 = {}
animals = sorted(["baboon", "lion", "tiger", "bat"])
print(animals)
counter = 1
# for species in animals:
#     index = animals.index(species)
#     if animals[index][0] == animals[index-1][0]:
#         zoo_dict[counter-1].append(species)
#
#     else:
#         zoo_dict[counter].append(species)
#         counter += 1
for species in animals:
    index = animals.index(species)
    if animals[index][0] == animals[index-1][0]:
        if (counter - 1) in zoo_dict1:
            zoo_dict1[counter - 1].append(species)
    else:
        zoo_dict1[counter] = [species]
        counter += 1
print(zoo_dict1[1])


# print(zoo_dict)
