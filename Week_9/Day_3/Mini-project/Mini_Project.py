class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    @staticmethod
    def basic_attack(self, enemy):
        enemy.life -= 1
        print(f"{enemy.name}'s life {self.life}")


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Ionnsaigh {self.name}")
        print(f"{self.name}, [life: {self.life}], [name: {self.life}]\n")

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, enemy):
        enemy.ife -= (0.75*self.life + 0.75*self.attack)


class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"skirskota {self.name} ")
        print(f"{self.name}, [life: {self.life}], [name: {self.attack}]\n")

    def brawl(self, enemy):
        enemy.life -= (2*self.attack)
        self.life += (0.5*self.attack)

    def train(self):
        self.attack += 2
        self.life += 2

    @staticmethod
    def roar(self, enemy):
        enemy.attack -= 3


class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Prahavate {self.name}")
        print(f"{self.name}, [life: {self.life}], [name: {self.attack}]\n")

    @staticmethod
    def curse(self, enemy):
        enemy.attack -= 2

    def summon(self):
        self.attack += 3
        # print(f"{self.name}'s life: {self.attack}")

    def cast_spell(self, enemy):
        enemy.life -= (self.attack/self.life)


Druid = Druid("Aoife")
Warrior = Warrior("Breki")
Mage = Mage("Shukra")

Mage.summon()


