# print("Functions")
# # numbers = [10, 20, 5]
# #
# #
# # def out_sum(*args):
# #     sum_of_numbers = 0
# #
# #     for num in args:
# #         sum_of_numbers = sum_of_numbers + num
# #     return sum_of_numbers
# #
# #
# # result = out_sum(10, 20, 5, 5, 20)
# # print(result)
# #
# #
# # def check_keyword_arguments(**kwargs):
# #     for key, value in kwargs.items():
# #         print(key, ":", value)
# #
# #
# # check_keyword_arguments(name="Sarah", age=24)
#
# valid_input = False
#
# while not valid_input:
#     try:
#         num1 = int(input("please enter the first parameter: "))
#         num2 = int(input("please enter the second parameter: "))
#         print(f"the result of the division is {num1 / num2}")
#     except ZeroDivisionError:
#         print("can't divide by zero")
#     except ValueError:
#         print("please enter an integer")
#     else:
#         valid_input = True
#     finally:
#         print("all of the code inside the finally will always run")
#
# print("Good bye")
#
# # def upper_string(s):
# # fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# #
# # print(f"Fruits before the change {fruit}")
# #
# # for i in range(len(fruit)):
# #     fruit[i] = upper_string(fruit[i])
# #
# # print(f"Fruits after the change{fruit}")
#
#
# def is_starts_with_a(s):
#     return s[0] == "A"
#
#
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# fruits_starts_with_a = []
#
# # for i in range(len(fruit)):
# #     print(i)
# #     if fruit[i][0] == "A":
# #         fruits_starts_with_a.append(fruit[i])
#
# fruits_starts_with_a = list(filter(is_starts_with_a(fruit)))
# print(f"Fruits starts with A are : {fruits_starts_with_a}")
# from functools import reduce
#
#
# def sum_numbers(first, second):
#     return first + second
#
#
# numbers = [1, 3, 4, 7]
#
# sum_of_numbers = 0
#
# sum_of_numbers = reduce(sum_numbers, numbers)
#
# print(sum_of_numbers)

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
name_length_less_than_4 = list(filter(lambda p: len(p) <= 4, people))
print(name_length_less_than_4)

new_name_list = list(map(lambda c: "Hello " + c, name_length_less_than_4))
print(new_name_list)
