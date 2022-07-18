# ------------------ Exercise 5 -------------- #
numbers = range(1, 21)

numbers_list = []
for number in numbers:
    numbers_list.append(number)
print(numbers_list)

myList = []
for number in numbers:
    index = numbers.index(number)
    if index % 2 == 0:
        myList.append(number)
print(myList)
