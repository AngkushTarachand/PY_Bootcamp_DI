print("Daily Challenge")


class Farm:

    def __int__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_name, num_of_animal=1):
        if num_of_animal <= 0:
            print("Invalid number")
        else:
            if animal_name in self.animals:
                self.animals.update({animal_name: num_of_animal})

    def farm_info(self):
        return f"{self.farm_name}'s farm"


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.farm_info())

