print("Exercise XP Week 6 Day 4")

# ------------------------ Exercise 11 --------------------- #
sandwich_orders = ["Tuna sandwich",
                   "Avocado sandwich",
                   "Egg sandwich",
                   "Sabih sandwich",
                   "Pastrami sandwich"]

finished_sandwiches = []

for order in sandwich_orders:
    is_ready = " "
    while is_ready is not "y":
        is_ready = input("is {} ready? if yes, enter y otherwise\
        enter n for no.".format(order))
    if is_ready is "y":
        finished_sandwiches.append(order)


sandwich_orders.clear()
print(finished_sandwiches)
print(sandwich_orders)
print("Finished")

for finished in finished_sandwiches:
    print("I made your {}".format(finished))
