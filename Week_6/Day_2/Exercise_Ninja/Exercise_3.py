print("Week 6 Day 2 ")

# -------------------- Exercise 3 ------------------------ #
print(3 <= 3 < 9)
# True because 3 is equal to 3 and less than 9.

print(3 == 3 == 3)
# True because they are of the same value and same data type.

print(bool(0))
# False because 0 is equal to False.

print(bool(5 == "5"))
# False because they are not of the same data type.

print(bool(4 == 4) == ("4" == "4"))
# True because bool( 4 == 4) is true as they are same data type and value
# and bool("4" == "4") is also true as they are same data type and value
# Hence bool(True == True) equals to True.

print(bool(bool(None)))
# False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is ", x)
print("y is ", y)
print("a: ", a)
print("b: ", b)
