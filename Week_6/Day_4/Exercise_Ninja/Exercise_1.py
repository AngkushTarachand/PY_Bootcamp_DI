import math
input_num = input("Enter number separated by ',': ")
print(input_num)

split_input = input_num.split(',')
print(split_input)

list_of_D = list(split_input)
print(list_of_D)

# list_of_D = list(map(int, input("Enter number").split(',')))
# print(list_of_D)
list_of_Q = []
for D in list_of_D:
    D = int(D)
    C = 50
    H = 30

    Q = round(math.sqrt((2*C*D)/H))
    list_of_Q.append(Q)

print(list_of_Q)



