# ---------------- Exercise 8 ----------- #
Exit_loop = False
Topping_list = []
while Exit_loop is False:
    Topping = input("Enter your pizza toppings. Enter quit to proceed to the total")
    if Topping != "quit":
        print(Topping + " has been added. ")
        Topping_list.append(Topping)
    else:
        Exit_loop = True

Total = 10 + len(Topping_list)*2.5
print("The total is ${}".format(Total))
