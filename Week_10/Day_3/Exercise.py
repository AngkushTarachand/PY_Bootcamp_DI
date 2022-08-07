# read line by line
for line in open('download.txt'):
    print(line)

# read 5th line
f = open("download.txt")
fifth = f.readline(5)
print("5th", fifth)

# read first 5 character
for x in range(5):
    print(f.read())

counter = 0
if "Drake" in f:
    counter += 1
print("counter", counter)

f = open("download.txt", mode="a+")
f.write("\nAngkush")
f.close()
