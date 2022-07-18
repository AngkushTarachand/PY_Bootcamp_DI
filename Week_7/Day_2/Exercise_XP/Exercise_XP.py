print("Exercise XP Week 7 Day 2")

# ------------------ Exercise 1 ------------------- #


def display_message():
    print("HELLO, I am following python at Developers' Institute")


display_message()

# ------------------- Exercise 2 --------------- #


def favorite_book(title):
    print("One of my favourite books is {}".format(title))


favorite_book("Purana")

# ------------------- Exercise 3 ----------------- #


def describe_city(city, country="Iceland"):
    print("{} is in {}".format(city, country))


describe_city("Mumbai", "India")

# ------------------- Exercise 4 --------------- #
import random


def guess_number(number):
    random_num1 = random.randint(1, 100)
    print(random_num1)
    if number is random_num1:
        print("Success")
    else:
        print("Unfortunely, it's a wrong guess."\
              "The number entered is {} and the random number is "\
              "{}".format(number, random_num1))


guess_number(input("Enter a number 1 and 100: "))

# ---------------------- Exercise 5 ---------------------------- #


def make_shirt(size, text):
    print("The size of the shirt is {} "\
          "and the text is {}".format(size, text))


make_shirt(input("Enter size of shirt"), input("Enter Text to be printed on shirt. "))


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


show_magicians(magician_names)


def make_great(magicians):
    make_great_list = list(map(lambda the_great: "The great " + the_great, magicians))
    print(make_great_list)


def show_magicians():
    make_great(magician_names)


show_magicians()

