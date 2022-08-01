#
#
# class Human:
#     def __init__(self, id_number, name, age, priority, blood_type):
#         self.id_number = id_number
#         # self.id_number = " "
#         self.name = name
#         # name = " "
#         self.age = age
#         # age = int
#         self.priority = priority
#         # priority = bool
#         self.blood_type = blood_type
#
#
# class Queue:
#     def __init__(self, humans):
#         self.humans = []
#
#     def add_person(self, person):
#         if person > 60 or self == True:
#             self.humans.insert(0, person.name)
#             print("added:", person, self.humans)
#         else:
#             self.humans.append(person.name)
#             print("added:", person.name, self.humans)
#
#     def find_in_queue(self, person):
#         print(self.humans.index(person.name))
#
#     def swap(self, person1, person2):
#         index1 = self.find_in_queue(person1)
#         index2 = self.find_in_queue(person2)
#         self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]
#         print(self.humans)
#
#     def get_next(self):
#         print("Next is", self.humans[0])
#
#     def get_next_blood_type(self, blood_type):
#         for human in self.humans:
#             if human.blood_type == blood_type:
#                 return self.humans.pop(human)
#
#     def sort_by_age(self):
#         if not self.humans:
#             self.humans.append(self.name)
#         else:
#             if self.priority:
#                 self.humans.index(0, self.name)
#             elif self.age >= 60:
#                 self.humans.append(self.name)
#             else:
#                 self.humans.insert(-1, self.name)
#         print("sorted:", self.humans)
#
#
# Agastya = Human("A102", "Agastya", 21, True, "AB")
# Aditya = Human("B093", "Aditya", 82, False, "A")
# Shiddhart = Human("H9495", "Shiddhart", 13, False, "AB")
# Kabir = Human("J49t5", "Kabir", 60, False, "AB")
#
# Queue.add_person(Agastya)
# Queue.add_person(Aditya)
# Queue.add_person(Shiddhart)
# Queue.add_person(Kabir)
#
# Agastya.find_in_queue(Agastya)
# Agastya.swap(Agastya, Kabir)
# Agastya.get_next()
# Agastya.get_next_blood_type("A")
# Agastya.sort_by_age()
