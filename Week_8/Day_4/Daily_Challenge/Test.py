names = ["Alice", "Bob", "Charlie", "David", "Emmanuel", "Fiona"]
counter = 0

while counter < len(names)-1:
    first_three = names[0+counter: 2+counter: 1]
    print(first_three)
    counter += 2
