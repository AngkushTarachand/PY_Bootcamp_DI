print("Week 6 Day 4 Exercise Gold")

# ----------- Exercise 9 -------------- #
import random
flag = False
counter_win = 0
counter_lost = 0

while flag is False:
    Num_input = input("Please enter a enter from 0 to 9"
                      "To quit enter q ")
    if Num_input is "q":
        print("Exit")
        flag = True
        break

    random_num = random.randint(1, 9)

    if int(Num_input) is random_num:
        print("Winner")
        counter_win += 1
    else:
        print("Game Lost")
        counter_lost += 1
print(counter_win)
print(counter_lost)
