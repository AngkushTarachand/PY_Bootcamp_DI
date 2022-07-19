print("Week 6 Day 4 Exercise Gold")

# ----------- Exercise 3 -------------- #
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Please enter your name: ")
if name in names:
    print(names.index(name))
else:
    print("Not in list")
