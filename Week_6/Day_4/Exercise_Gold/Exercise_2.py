print("Week 6 Day 4 Exercise Gold")

# ----------- Exercise 2 -------------- #
x = range(1500, 2501)
for each in x:
    if each % 5 is 0:
        print("{} is a multiple of 5 ".format(each))
    elif each % 7 is 0:
        print("{} is a multiple of 7 ".format(each))
print("Finished")
