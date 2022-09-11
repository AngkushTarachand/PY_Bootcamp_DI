from random import randint

num_list = [[3, 47, 99, -80, 22, 97, 54, -23, 5, 7],
            [44, 91, 8, 24, -6, 0, 56, 8, 100, 2],
            [3, 21, 76, 53, 9, -82, -3, 49, 1, 76],
            [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]]

list_1 = []
for each in num_list:
    list_1 += each

print(list_1)
print(sorted(list_1, reverse=True))
print(sum(list_1))

num_list_start_end = []
for each in num_list:
    num_list_start_end.append(each[0])
    num_list_start_end.append(each[len(each) - 1])

print("Start and end list: ", num_list_start_end)

greater_than_50_list = []
for each in list_1:
    if each > 50:
        greater_than_50_list.append(each)

print("Greater than 50 list: ", greater_than_50_list)

smaller_than_10_list = []
for each in list_1:
    if each < 10:
        smaller_than_10_list.append(each)

print("smaller than 10 list:\t", smaller_than_10_list)

result = list(map(lambda x: x * x, list_1))
print("square list:\t\t\t", result)

unique_list = list(set(list_1))
print("unique list:\t\t\t", unique_list)

average = round(sum(list_1) / len(list_1))
print("average:\t\t\t\t", average)

largest = max(list_1)
print("Largest number: ", largest)

smallest = min(list_1)
print("Smallest number: ", smallest)

num = 0
for each in list_1:
    num += each
print(num, sum(list_1))

bonus_average = num / len(list_1)

print("Enter")
sorted_list = []

greatest = list_1[0]
for each in list_1:
    if each > greatest:
        greatest = each
print(greatest, max(list_1))

smallest_1 = list_1[0]
for each in list_1:
    if each < smallest_1:
        smallest_1 = each

print(smallest_1, min(list_1))

counter = 0
sub = 0
flag = False
# while counter < 10:
#     counter += 1
#     while sub < 10:
#         sub += 1
#         while not flag:
#             num = int(input("Please enter a number between -100 to 100"))
#             if -100 >= num >= 100:
#                 flag = True

# for n in range(1):
#     # while not flag:
#     num = input("Please enter 10 number between 100 and -100 ")
#     num_list_bonus = num.split(',')
#     list_to_int = list(map(int, x) for x in num_list_bonus)
# list_num = list(map(lambda x:  x > 100, list_to_int))
# if list_num:
#     flag = True

list_rand = []
counter_bonus_1 = 0
while counter_bonus_1 < 10:
    counter_bonus_1 += 1
    x = randint(-100, 100)
    list_rand.append(x)
print(list_rand)

list_rand_2 = []
counter_limit = randint(0, 50)
counter_bonus_2 = 0
while counter_bonus_2 < counter_limit:
    counter_bonus_2 += 1
    x = randint(-100, 100)
    list_rand_2.append(x)
print(list_rand_2)

# Will the code work when the number of random numbers is not equal to 10?
# It will not work as the iteration start at 0 after than 10 loop it\
# will on the 10th loop but the number of the loop will be 9
