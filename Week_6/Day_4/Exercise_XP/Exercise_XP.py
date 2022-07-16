# print("Exercise XP Week 6 Day 4")
#
# # --------------- Exercise 1 --------------------#
# my_fav_numbers = {2, 7, 14}
#
# my_fav_numbers.add(26)
# my_fav_numbers.add(8)
#
# print(my_fav_numbers)
#
# friend_fav_numbers = {19, 11, 20}
# print(friend_fav_numbers)
#
# our_favourite_numbers = my_fav_numbers.union(friend_fav_numbers)
#
# print(our_favourite_numbers)
#
# # ------------- Exercise 2 ------------------- #
#
# tuple1 = (1, 2, 3, 4)
# # Tuples are immutable, new values can't be added
#
# # ------------- Exercise 3 ------------------- #
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#
# basket.remove("Banana")
# print(basket)
#
# basket.remove("Blueberries")
# print(basket)
#
# basket.append("Kiwi")
# print(basket)
#
# basket.insert(0, "Apples")
# print(basket)
#
# NumOfApple = 0
#
# for fruit in basket:
#     if "Apples" == fruit:
#         NumOfApple = NumOfApple + 1
# print(NumOfApple)
#
# x = basket.count("Apples")
# print(x)
#
# basket.clear()
# print(basket)
#
# # ------------------ Exercise 5 -------------- #
# numbers = range(1, 21)
#
# numbers_list = []
# for number in numbers:
#     numbers_list.append(number)
# print(numbers_list)
#
# myList = []
# for number in numbers:
#     index = numbers.index(number)
#     if index % 2 == 0:
#         myList.append(number)
# print(myList)
#
# # ---------------- Exercise 6 ----------- #
# status = False
# while status is False:
#     username = input("Please enter your name")
#     if username == "Angkush":
#         status = True
#
#     else:
#         status = False
# print("Finished")
#
# # ---------------- Exercise 7 ----------- #
# Fav_fruits = input("Please input your favourite fruits ")
#
# Fav_fruits_list = Fav_fruits.split()
#
# print(Fav_fruits_list)
#
# fruit = input("Please input your fruits ")
#
# if fruit in Fav_fruits_list:
#     print("You choose your favourite fruit")
# else:
#     print("You chose a new fruit. ")
#
# # ---------------- Exercise 8 ----------- #
# Exit_loop = False
# Topping_list = []
# while Exit_loop is False:
#     Topping = input("Enter your pizza toppings. Enter quit to proceed to the total")
#     if Topping != "quit":
#         print(Topping + " has been added. ")
#         Topping_list.append(Topping)
#     else:
#         Exit_loop = True
#
# Total = 10 + len(Topping_list)*2.5
# print("The total is ${}".format(Total))
#
# # ---------------- Exercise 9 ----------- #
#
# NumOfPeople = input("Enter the numer of people ")
# NumOfPeople = int(NumOfPeople)
# x = 0
# counter1 = 0
# counter2 = 0
# counter3 = 0
#
# while x < NumOfPeople:
#     age = input("Enter the age of the person")
#     age = int(age)
#     if age < 3:
#         print("The ticket is free")
#         counter1 = counter1 + 1
#     elif 3 <= age <= 12:
#         print("The ticket is $10")
#         counter2 = counter2 + 1
#     else:
#         print("The ticket is $15")
#         counter3 = counter3 + 1
#     x = x + 1
#
# Total = counter1*0 + counter2*10 + counter3*15
# print("The total is {}".format(Total))
#
# name_list = ["Raj", "Ram", "Abhi"]
# for teenager in name_list:
#     age1 = int(input("Please enter {} age".format(teenager)))
#     if 16 <= age1 <= 21:
#         name_list.remove(teenager)
# print(name_list)

# ---------------- Exercise 9 ----------- #
# sandwich_orders = ["Tuna sandwich",
#                    "Avocado sandwich",
#                    "Egg sandwich",
#                    "Sabih sandwich",
#                    "Pastrami sandwich"]
#
# finished_sandwiches = []
#
# for order in sandwich_orders:
#     # isReady = input("Is {} ready, y or n".format(order))
#     # if isReady is "y":
#     finished_sandwiches.append(order)
#     sandwich_orders.remove(order)
#
# print(finished_sandwiches)
# print(sandwich_orders)
# print("Finished")
#
# for finished in finished_sandwiches:
#     print("I made your {}".format(finished))

# ------------------------ Exercise 11 --------------------- #
print("deli has run out of pastrami")
sandwich_orders1 = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
                    "Pastrami sandwich", "Egg sandwich",
                    "Sabih sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders1:
    sandwich_orders1.remove("Pastrami sandwich")

print(sandwich_orders1)
