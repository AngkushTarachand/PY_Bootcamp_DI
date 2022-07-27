class Documentation:
    def __init__(self, number):
        self.num = number
        self.document = " "

    def __int__(self):
        """It converts a digit defined string into a number"""
        return self.num

    def __abs__(self):
        """It outputs the absolute of number"""
        return abs(self.num)

    def __input__(self):
        """It prompts the users to enter a data"""
        self.document = input("Enter a data")


d1 = Documentation(15)
print(d1.__abs__())
print(d1.__int__.__doc__)


