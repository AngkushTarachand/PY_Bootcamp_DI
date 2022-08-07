import functools
import operator
from itertools import permutations


class AnagramChecker:
    def __init__(self):
        with open("words.txt") as file:
            list_file = []
            for line in file:
                list_file.append(line.strip())
            print(list_file)
        self.word_list = list_file

    def is_valid_word(self, word):
        if word in self.word_list:
            print("Found")
        else:
            print("Not Found")

    def get_anagrams(self, word):
        for each in self.word_list:
            word_list_set = set(each)
            if set(word) == word_list_set and len(word) == len(each):
                print(each)

    @staticmethod
    def is_anagrams(word1, word2):
        word1_set = set(word1)
        word2_set = set(word2)
        if word1_set == word2_set:
            print("TRUe")
        else:
            print("False")


v = AnagramChecker()
v.is_valid_word("ZZZ")
v.get_anagrams("ABACUS")
v.is_anagrams("BRERES", "BRERS")
