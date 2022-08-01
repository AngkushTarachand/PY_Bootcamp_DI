

class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack
        self.character_dict = {}

    @staticmethod
    def basic_attack(enemy):
        enemy.life -= 1
        print(f"{enemy.name}'s life {enemy.life}")

    def display(self):
        self.character_dict = {"life": self.life, "attack": self.attack}
        # print(self.name + str({"life": self.life, "attack": self.attack}))
        print(self.name, self.character_dict)


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Ionnsaigh {self.name}")
        self.name = name
        self.life = life
        self.attack = attack
        # print(f"{self.name}, [life: {self.life}], [attack: {self.attack}]\n")

    def meditate(self):
        self.life += 10
        print(self.life)
        self.attack -= 2
        self.character_dict["life"] = self.life
        # print("mediate =>", self.life, self.attack)

    def animal_help(self):
        self.attack += 5
        # print("animal help =>", self.attack)

    def fight(self, other):
        other.life -= round(0.75*self.life + 0.75*self.attack)
        # print("fight =>", other.life)


class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        self.name = name
        self.life = life
        self.attack = attack
        print(f"skirskota {self.name} ")
        print(f"{self.name}, [life: {self.life}], [name: {self.attack}]\n")

    def brawl(self, other):
        other.life -= (2*self.attack)
        self.life += (0.5*self.attack)
        print("brawl =>", other.name, other.life, self.name, self.life)

    def train(self):
        self.attack += 2
        self.life += 2
        print(self.attack, self.life)

    @staticmethod
    def roar(other):
        other.attack -= 3
        print(other.name, other.attack)


class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Prahavate {self.name}")
        print(f"{self.name}, [life: {self.life}], [name: {self.attack}]\n")

    @staticmethod
    def curse(other):
        other.attack -= 2
        print("attack =>", other.name, other.attack)

    def summon(self):
        self.attack += 3
        print("summon => " + f"{self.name}'s life: {self.attack}")

    def cast_spell(self, other):
        other.life -= (self.attack/self.life)
        print("cast spell =>", other.name, other.life)


druid = Druid("Aoife")

warrior = Warrior("Breki")

mage = Mage("Shukra")
druid.meditate()

druid.display()
warrior.display()
mage.display()




#
# print("testing for Mage")
# mage.summon()
# mage.cast_spell(druid)
# mage.curse(druid)
#
# print("\ntesting for Druid")
# druid.fight(warrior)
# druid.meditate()
# druid.animal_help()
#
# print("\ntesting for warrior")
# warrior.brawl(mage)
# warrior.train()
# warrior.roar(druid)
#
# warrior.basic_attack(druid)
# character_list =[]
# for each in Character:
#     character_list.append(each)
#     print(each)

