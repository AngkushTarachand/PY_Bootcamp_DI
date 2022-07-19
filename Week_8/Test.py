class Farm:
	def __init__(self, name):
		self.name = name
		self.animals = {}

	def add_animal(self, animal_name, num_of_animal=1):
		if num_of_animal <= 0:
			print("Invalid number")
		else:
			if animal_name not in self.animals.keys():
				self.animals[animal_name] = num_of_animal

			elif animal_name in self.animals.keys() and num_of_animal is 1:
				num_of_animal = num_of_animal + 1
				self.animals.update({animal_name: num_of_animal})
			# else:
				# self.animals[num_of_animal] = self.animals[num_of_animal] + num_of_animal

	def get_info(self):
		result = f"""{self.name}'s farm"""
		for key in self.animals:
			result += f"{key}: {self.animals[key]}"
		result += "\t E - I - E - I - 0 "


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
