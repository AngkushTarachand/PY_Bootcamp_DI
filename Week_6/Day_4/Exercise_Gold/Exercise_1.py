print("Week 6 Day 4 Exercise Gold")

# ----------- Exercise 1 -------------- #
list_1 = ['a', 'b', 'c']
list_2 = ["1", "2", "3"]
print(list_1)
print(list_2)
# concatenate_list = list_1.extend(list_2)
concatenate_list = [*list_2, *list_1]
# print(list_1.extend(list_2))
print(concatenate_list)
