import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = round(math.pi*(self.radius**2))
        # circle_area = math.pi*self.radius*self.radius
        return circle_area

    def __add__(self, other):
        return self.radius + other.radius

    def __ge__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


def listing(circles):
    print("Testing")
    for circle in circles:
        print(str(circle))


circle1 = Circle(2)
circle2 = Circle(5)
circle3 = Circle(2)
my_circles = [circle1, circle2, circle3]

print("before sorting")
listing(my_circles)

# sort_my_list = sorted(my_circles)
# listing(sort_my_list)

print(circle1.__eq__(circle3))

