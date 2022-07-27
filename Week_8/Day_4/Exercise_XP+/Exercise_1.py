
class Family:
    def __init__(self, members, last_name):
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]
        self.last_name = last_name
        self.members["age"]

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



