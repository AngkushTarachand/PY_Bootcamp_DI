

print("Daily Challenge")

# matrix = ["7", "T", "h", "i", "s", "$", "#"]

matrix = [
    "7i3",
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

column_length = len(matrix[0])
row_length = len(matrix)
print(row_length)
print(column_length)
decrypt = []
print(matrix[0][0])
counter = 0
column_counter = 0

# while counter < row_length:
#     print(matrix[counter][0])
#     if matrix[counter][0].isalnum() is True:
#         decrypt.append(matrix[counter][0])
#
#         print(counter)
#     counter = counter + 1
# print("Next test")
# for each in range(0, column_length):
#     # Checking each row
#     while counter < row_length:
#         print(matrix[counter][each])
#         if matrix[counter][each].isalnum() is True:
#             decrypt.append(matrix[counter][each])
#         counter = counter + 1
#     column_counter = column_counter + 1


decoded = ''

rows_len = len(matrix)
column_len = len(matrix[0])
to_add_space = False

for column_num in range(column_len):
    for row_num in range(rows_len):
        if matrix[row_num][column_num].isalpha():
            decoded += matrix[row_num][column_num]
            to_add_space = True
        elif to_add_space:
            decoded += " "
            to_add_space = False

print(decoded.strip())
