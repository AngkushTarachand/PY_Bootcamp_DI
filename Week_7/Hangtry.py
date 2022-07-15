import random

words_list = \
    ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
     'credit card', 'rush', 'south']

word = random.choice(words_list)

length_word = len(word)
print(word)
print(length_word)

# Listify the word
word_list = list(word)
guess_word_list = []

# Generate the blank spaces of that word
for character in word:
    guess_word_list.append("-")

print(word_list)
print(guess_word_list)

# Replace character input into guess world list
counter = 0
while counter < length_word:
    character_input = input("Enter character: ")
    if character_input in word_list:
        if character_input in guess_word_list:
            print("Already Entered. Try again")
        else:
            index = word_list.index(character_input)
            guess_word_list[index] = character_input
            print(guess_word_list)
    else:
        print("Wrong Input")
    counter = counter + 1

if guess_word_list is words_list:
    print("Congrats")
else:
    print("Hangout")







