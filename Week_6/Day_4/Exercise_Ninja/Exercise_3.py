paragraph = "Hindus believe in the doctrines of samsara (the continuous cycle of life, death, and reincarnation) and " \
            "karma (the universal law of cause and effect). One of the key thoughts of Hinduism is “atman," \
            "” or the belief in soul. This philosophy holds that living creatures have a soul, and they're all part " \
            "of the supreme soul."

characters = len(paragraph)
print(characters)
sentence = paragraph.split(".")
print(sentence)
num_of_sentence = len(sentence)
print(num_of_sentence)
words = paragraph.split(" ")
print(words)
num_of_words = len(words)
print(num_of_words)
unique_word = set(words)
print(unique_word)
num_of_unique_word = len(unique_word)
print(num_of_unique_word)


white_space = " "

counter_whitespace = 0
for each in paragraph:
    if white_space == each:
        counter_whitespace += 1

print(counter_whitespace)

average_word_per_sentence = num_of_words/num_of_sentence
print(average_word_per_sentence)

num_of_non_unique_words = num_of_words - num_of_unique_word
print(num_of_non_unique_words)

print(f"The paragraph has {characters} characters, {num_of_sentence} sentences, "
      f"{num_of_words} words, "
      f"{num_of_unique_word} unique words")

