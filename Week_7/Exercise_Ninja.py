print("Exercise Ninja")
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
#  ------------------- Exercise 4 ------------------------ #
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," \
          "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."\
           "Ut enim ad minim veniam, quis nostrud exercitation ullamco"\
           "laboris nisi ut aliquip ex ea commodo consequat."\
           "Duis aute irure dolor in reprehenderit in voluptate velit"\
           "esse cillum dolore eu fugiat nulla pariatur."\
           "Excepteur sint occaecat cupidatat non proident,"\
           "sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

# ------------------ Exercise 5 --------------------------#

sentence = input("Please enter a sentence without character 'A' ")

if sentence.find("A") == -1:
    new_record = 0
    if len(sentence) > new_record:
        print("New longest sentence")
        new_record = len(sentence)
    else:
        print("Try Again")
else:
    print("Sorry contains 'A' ")
