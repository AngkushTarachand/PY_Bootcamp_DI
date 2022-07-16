import random
print("Daily Challenge")

word = " "

while len(word) < 10:
    word = input("Please enter a word at least 10 character long: ")
    # if len(word) < 10:
    #     print("String not enough long.")
    # elif len(word) > 10:
    #     print("String too long.")

print(word[:1])
print(word[len(word) - 1: len(word)])

counter = 0
while counter < len(word):
    counter = counter + 1
    print(word[0:counter])



