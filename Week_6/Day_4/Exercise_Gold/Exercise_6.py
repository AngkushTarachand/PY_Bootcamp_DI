word_list = []
counter = 0
while counter < 2:
    counter += 1
    word = input("Enter enter a word: ")
    word_list.append(word)
print(word_list)
letter_input = ""
while len(letter_input) is not 1:
    letter_input = input("Please enter a letter: ")

for word in word_list:
    if letter_input in word:
        print(word.index(letter_input))
    else:
        print("Sorry try next time")



