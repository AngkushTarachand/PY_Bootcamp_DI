print("Week 6 Day 4 Exercise Gold")

# ----------- Exercise 1 -------------- #
# list_1 = ['a', 'b', 'c']
# list_2 = ["1", "2", "3"]
# print(list_1)
# print(list_2)
# # concatenate_list = list_1.extend(list_2)
# concatenate_list = [*list_2, *list_1]
# # print(list_1.extend(list_2))
# print(concatenate_list)

# ----------- Exercise 2 -------------- #
# x = range(1500, 2501)
# for each in x:
#     if each % 5 is 0:
#         print("{} is a multiple of 5 ".format(each))
#     elif each % 7 is 0:
#         print("{} is a multiple of 7 ".format(each))
# print("Finished")

# ----------- Exercise 3 -------------- #
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#
# name = input("Please enter your name: ")
# if name in names:
#     print(names.index(name))
# else:
#     print("Not in list")

# ----------- Exercise 4 -------------- #
# counter = 0
# number_list = []
# while counter < 3:
#     counter += 1
#     order = ["1st", "2nd", "3rd"]
#     num_input = int(input("Enter number {}: ".format(order[counter-1])))
#     number_list.append(num_input)
#     number_list.sort()
# print(number_list[len(number_list)-1])

# ----------- Exercise 5 -------------- #
# alphabet ="abcdefghijklmnopqrstuvwxyz"
# vowel_list = ["a", "e", "i", "o", "u"]
# for letter in alphabet:
#     if letter in vowel_list:
#         print("{} is a vowel".format(letter))
#     else:
#         print("{} is a consonant".format(letter))

# ----------- Exercise 6 -------------- #
# word_list = []
# counter = 0
# while counter < 2:
#     counter += 1
#     word = input("Enter enter a word: ")
#     word_list.append(word)
# print(word_list)
# letter_input = ""
# while len(letter_input) is not 1:
#     letter_input = input("Please enter a letter: ")
#
# for word in word_list:
#     if letter_input in word:
#         print(word.index(letter_input))
#     else:
#         print("Sorry try next time")

# ----------- Exercise 6 -------------- #
# num_list = []
#
# num = range(1, 1000001)
# for each in num:
#     num_list.append(each)
#
# min(num_list)
# print(min(num_list))
#
# max(num_list)
# print(max(num_list))
#
# total = sum(num_list)
# print(total)
# ----------- Exercise 7 -------------- #
# sequence = input("Enter a sequence separated by ','")
#
# print(sequence)
# ----------- Exercise 8 -------------- #
# import random
# flag = False
# counter_win = 0
# counter_lost = 0
#
# while flag is False:
#     Num_input = input("Please enter a enter from 0 to 9"
#                       "To quit enter q ")
#     if Num_input is "q":
#         print("Exit")
#         flag = True
#         break
#
#     random_num = random.randint(1, 9)
#
#     if int(Num_input) is random_num:
#         print("Winner")
#         counter_win += 1
#     else:
#         print("Game Lost")
#         counter_lost += 1
# print(counter_win)
# print(counter_lost)
