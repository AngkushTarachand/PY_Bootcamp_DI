# ---------------- Exercise 7 ----------- #
Fav_fruits = input("Please input your favourite fruits ")

Fav_fruits_list = Fav_fruits.split()

print(Fav_fruits_list)

fruit = input("Please input your fruits ")

if fruit in Fav_fruits_list:
    print("You choose your favourite fruit")
else:
    print("You chose a new fruit. ")
