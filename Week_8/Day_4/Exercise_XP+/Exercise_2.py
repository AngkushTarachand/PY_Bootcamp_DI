class Family:
    def __int__(self, members, last_name):
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(**kwargs)

    def is_18(self):
        if self.age > 18:
            return True
        else:
            return False
    def family_representation(self):
        for each in self.members:
            print("{} {}".format(self.members[each].get("name"), self.last_name))


class TheIncredibles(Family):
    def use_power(self):
        for each in len(self.members):
            if self[each].age > 18:
                print([each].name, [each].powers)

    def incredible_presentation(self):
        super().family_representation()
        for member in len(self.members):
            print(self.members[member].name, self.members[member].powers)

    incredible_presentation().born
