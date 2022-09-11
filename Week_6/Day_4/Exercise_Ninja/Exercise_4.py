sentence = "New to Python or choosing between " \
           "Python 2 and Python 3? Read Python 2 or Python 3."

sentence_list = sentence.split(" ")

freq = {}

for item in sentence_list:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1


for key, value in freq.items():
    print(key, value)
