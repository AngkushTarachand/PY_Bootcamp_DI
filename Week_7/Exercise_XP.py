# --------------------- Exercise 1 ---------------------- #

print("Hello world\nHello world\nHello world\nHello world\nHello world")


# --------------------- Exercise 2 ---------------------- #
print((99**3)*8)

# --------------------- Exercise 3 ---------------------- #
print(bool(5 < 3))
# The output will be false as 5 is greater than 3
print(bool(3 == 3))
# The output will be true as 3 is an integer and are equal
# print(bool(3 == "3"))
# There will be no output as the data type are difference hence cannot be changed
# print(bool("3" > 3))
# There will be no output as the data type are difference hence cannot be changed
print("Hello" == "hello")
# The output will be false as despite the data type is the same but the value is not.

# ---------------- Exercise 4 ------------------------- #

computer_brand = "Omen"

print("I have a {} computer".format(computer_brand))

name = "Angkush"

age = 20

shoe_size = 43

info = "I am {}, {} years old model and my shoe size is {}".format(name, age, shoe_size)

print(info)

# ------------- Exercise 5 -------------- #

a = 5
b = 3

if a > b:
    print("Hello World")

# -------------- Exercise 7 -------------- #
digit = int(input("Enter a number"))
print(type(digit))

if digit % 2 == 0:
    print("{] is even".format(digit))
else:
    print("{} is odd".format(digit))

# -------------- Exercise 8 -----------------#

name = "Angkush"

username = str(input("Enter your name"))

if username == name:
    print("Why you do name the same name as mine")
else:
    print("Thanks, we don't have the same name")

# ----------------- Exercise 9 ---------------- #
username_height = int(input("Enter your height in inches"))

if username_height*2.54 > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride")
