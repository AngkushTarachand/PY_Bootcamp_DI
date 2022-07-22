class Circle:
    color = "red"


class NewCircle(Circle):
    color = "blue"


nc = NewCircle
print(nc.color)

# What will be the output ?
# Output : blue
