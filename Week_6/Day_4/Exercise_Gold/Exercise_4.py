print("Week 6 Day 4 Exercise Gold")

# ----------- Exercise 4 -------------- #
counter = 0
number_list = []
while counter < 3:
    counter += 1
    order = ["1st", "2nd", "3rd"]
    num_input = int(input("Enter number {}: ".format(order[counter-1])))
    number_list.append(num_input)
    number_list.sort()
print(number_list[len(number_list)-1])
