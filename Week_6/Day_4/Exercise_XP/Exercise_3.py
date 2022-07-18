print("Exercise XP Week 6 Day 4")

# ------------- Exercise 3 ------------------- #
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)

NumOfApple = 0

for fruit in basket:
    if "Apples" == fruit:
        NumOfApple = NumOfApple + 1
print(NumOfApple)

x = basket.count("Apples")
print(x)

basket.clear()
print(basket)
