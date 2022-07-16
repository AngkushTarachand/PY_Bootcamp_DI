# ------------------------ Exercise 11 --------------------- #
print("deli has run out of pastrami")
sandwich_orders1 = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
                    "Pastrami sandwich", "Egg sandwich",
                    "Sabih sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders1:
    sandwich_orders1.remove("Pastrami sandwich")

print(sandwich_orders1)
