# ------------- Daily_challenge 2 -------------- #
word = input("Enter enter a word: ")
word_list = list(word)
uniq = []
counter = 0
while counter < len(word_list):
    if counter is 0:
        uniq.append(word_list[counter])

    elif counter > 0:
        if word_list[counter] is not word_list[counter - 1]:
            uniq.append(word_list[counter])
    counter = counter + 1
print(''.join(uniq))
