from collections import Counter


class Text:
    def __init__(self, text):
        self.text = text

    def frequency(self, word):
        if word in self.text:
            counter = 0
            counter += 1
            return counter

    def most_common(self):
        split_it = self.text.split()

        counter = Counter(split_it)

        most_occur = counter.most_common()

        return most_occur[0]

    def unique(self):
        for each in most_occur:
            if each[1] == 1:
                print(each)


t = Text("Hello it was wandering whenther hello is good to say hello")
t.most_common()
t.unique()
