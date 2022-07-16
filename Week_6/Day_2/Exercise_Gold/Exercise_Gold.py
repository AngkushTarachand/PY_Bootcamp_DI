print("Gold Exercise")
# ------------------ Exercise 1 ------------------ #
print("Hello World \n Hello World \n Hello World \n World\n"
      "I love python\n I love python \n I love python \n I love python")

# ------------------- Exercise 2 ------------------ #
month = int(input("Enter a month number( 1 to 12): "))
if 3 <= month <= 5:
    print("Spring runs from March(3) to May(5)")
elif 6 <= month <= 8:
    print("Summer runs from June(6) to August(8)")
elif 9 <= month <= 11:
    print("Autumn runs from September (9) to November (11)")
elif 0 < month < 3 or month is 12:
    print("Winter runs from December(12) to February(2)")
