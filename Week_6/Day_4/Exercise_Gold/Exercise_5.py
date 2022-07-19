print("Week 6 Day 4 Exercise Gold")

# ----------- Exercise 5 -------------- #
alphabet ="abcdefghijklmnopqrstuvwxyz"
vowel_list = ["a", "e", "i", "o", "u"]
for letter in alphabet:
    if letter in vowel_list:
        print("{} is a vowel".format(letter))
    else:
        print("{} is a consonant".format(letter))
