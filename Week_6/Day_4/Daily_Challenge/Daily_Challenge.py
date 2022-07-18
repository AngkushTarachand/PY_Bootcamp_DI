# ------------- Daily_challenge 1 -------------- #
num = int(input("Enter a number"))

length = int(input("Please enter number for length "))

counter = 0
num_list = []
while counter < length:
    counter = counter + 1
    multiple_num = counter*num
    num_list.append(multiple_num)

print("number: {} - length {} => {}".format(num, length, str(num_list)))
