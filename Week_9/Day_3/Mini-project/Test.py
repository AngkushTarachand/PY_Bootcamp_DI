class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    @staticmethod
    def basic_attack(self, enemy):
        enemy.life -= 1


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        self.name = name
        self.life = life
        self.attack = attack
        print(f"Ionnsaigh {self.name}")

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, enemy):
        enemy.life -= (0.75*self.life + 0.75*self.attack)


class Warrior(Character):
    def __init__(self, name, life=20, attack=1):
        super().__init__(name, life, attack)
        print(f"shirskoka {self.name}")

    def brawl(self, enemy):
        enemy.life -= (2*self.attack)
        self.life += (0.5*self.attack)
        print(enemy.life)

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

    @staticmethod
    def curse(self, enemy):
        enemy.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, enemy):
        enemy.life -= (self.attack/self.life)


Druid = Druid("Aoife")
Warrior = Warrior("Breki")
Mage = Mage("Shukra")

Mage.curse(Druid.life)
