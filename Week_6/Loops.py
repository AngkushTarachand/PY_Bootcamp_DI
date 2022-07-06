flag = True
while flag:
    num = input("Please enter a number: ")
    num = int(num)

    if num > 0:
        flag = False
        print("Congratulation!")
    else:
        print("Number is not positive")
# Advanced Loops
# For Loops with steps
# range(start, Stop, Step)

for num in range (1, 20, 3):
    print(num)

odd_num = list(range(1, 20, 2))
print(odd_num)

alphabet = "abcdefgh"
for a in alphabet:
    print(a)

for idx in range(len(alphabet)):
    print(idx, alphabet[idx])

# nt(item)  # tuple (index, value)

for (idx, val) in enumerate(alphabet):
    print(idx, val)
    print('At index {} the value is {}'. format(idx, val))

# Zip

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

for item in zip(list1, list2, list3):
    print(item)  # Returns a tuple containing the item at the same index from each list

# For - Else
# Else is optional - executed once after the loop (except)

# for num in range(1, 20 , 3):
#     print(num)
#     num == 10:
#     break
# else:
#     print('All odd numbers generated' # Executed only if break is not encountered
#
# print('For-else loop completed')

# while-Else
x = 0
while x < 10:
    print(x)
    x +=1
else:
    print('x is not smaller than 10. x is ) ' + str(x))

print('While loops completed')

# for student in List1:
#     # retrieve data from database


