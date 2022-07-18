print("Week 6 Day 2 ")

# ------------------ Exercise 5 --------------------------#

sentence = input("Please enter a sentence without character 'A' ")

new_record = 0

if sentence.find("A") == -1:

    if len(sentence) > new_record:
        print("New longest sentence")
        new_record = len(sentence)
        sentence = input("Please enter a sentence without character 'A' ")

    else:
        print("Try Again")

else:
    print("Sorry contains 'A' ")

# print(''.join(random.sample(word, len(word))))
