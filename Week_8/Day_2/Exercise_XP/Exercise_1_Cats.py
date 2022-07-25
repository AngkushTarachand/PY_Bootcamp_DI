
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        self.cats = {}


cat1 = Cat("M", 4)
cat2 = Cat("N", 3)
cat3 = Cat("O", 2)


def find_old_cat():
    if cat1.age > cat2.age:
        if cat1.age > cat3.age:
            oldest = cat1
        else:
            oldest = cat3
    else:
        if cat2.age > cat3.age:
            oldest = cat2
        else:
            oldest = cat3
    print(f"The oldest cat is {oldest.name} and is {oldest.age}")


find_old_cat()



