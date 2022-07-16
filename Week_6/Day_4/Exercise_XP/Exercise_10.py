sandwich_orders = ["Tuna sandwich",
                   "Avocado sandwich",
                   "Egg sandwich",
                   "Sabih sandwich",
                   "Pastrami sandwich"]

finished_sandwiches = []

for order in sandwich_orders:
    # isReady = input("Is {} ready, y or n".format(order))
    # if isReady is "y":
    finished_sandwiches.append(order)
    sandwich_orders.remove(order)

print(finished_sandwiches)
print(sandwich_orders)
print("Finished")

for finished in finished_sandwiches:
    print("I made your {}".format(finished))